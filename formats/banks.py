# -*- coding: utf-8 -*-


class FormatBank(object):

    def __init__(self, discover=False, exclude=None):
        """Creates a new `FormatBank` object and optionally discovers
        installed formats.

        :param discover: (optional) When ``True``, formats are
            automatically discovered
        :param exclude: (optional) Exclude formats from being discovered.
        """
        self.registered_formats = {}
        if discover:
            self.discover(exclude)

    def register(self, type, parser, composer, **meta):
        """Registers a parser and composer of a format.

        You can use this method to overwrite existing formats.

        :param type: The unique name of the format
        :param parser: The method to parse data as the format
        :param composer: The method to compose data as the format
        :param meta: The extra information associated with the format
        """
        self.registered_formats[type] = {
            'parser': parser,
            'composer': composer,
            'meta': meta,
        }

    def register_parser(self, type, parser, **meta):
        """Registers a parser of a format.

        :param type: The unique name of the format
        :param parser: The method to parse data as the format
        :param meta: The extra information associated with the format
        """
        try:
            self.registered_formats[type]['parser'] = parser
        except KeyError:
            self.registered_formats[type] = {'parser': parser}
        if meta:
            self.register_meta(type, **meta)

    def register_composer(self, type, composer, **meta):
        """Registers a composer of a format.

        :param type: The unique name of the format
        :param composer: The method to compose data as the format
        """
        try:
            self.registered_formats[type]['composer'] = composer
        except KeyError:
            self.registered_formats[type] = {'composer': composer}
        if meta:
            self.register_meta(type, **meta)

    def register_meta(self, type, **meta):
        """Registers extra _meta_ information about a format.

        :param type: The unique name of the format
        :param meta: The extra information associated with the format
        """
        try:
            self.registered_formats[type]['meta'] = meta
        except KeyError:
            self.registered_formats[type] = {'meta': meta}

    def parser(self, type, **meta):
        """Registers the decorated method as the parser of a format.

        :param type: The unique name of the format
        :param meta: The extra information associated with the format
        """
        def decorator(f):
            self.register_parser(type, f)
            if meta:
                self.register_meta(type, **meta)
            return f
        return decorator

    def composer(self, type, **meta):
        """Registers the decorated method as the composer of a format.

        :param type: The unique name of the format
        :param meta: The extra information associated with the format
        """
        def decorator(f):
            self.register_composer(type, f)
            if meta:
                self.register_meta(type, **meta)
            return f
        return decorator

    def parse(self, type, data):
        """Parse text as a format.

        :param type: The unique name of the format
        :param data: The text to parse as the format
        """
        try:
            return self.registered_formats[type]['parser'](data)
        except KeyError:
            raise NotImplementedError("No parser found for "
                                      "type '{type}'".format(type=type))

    def compose(self, type, data):
        """Compose text as a format.

        :param type: The unique name of the format
        :param data: The text to compose as the format
        """
        try:
            return self.registered_formats[type]['composer'](data)
        except KeyError:
            raise NotImplementedError("No composer found for "
                                      "type '{type}'".format(type=type))

    def convert(self, type_from, type_to, data):
        """Parsers data from with one format and composes with another.

        :param type_from: The unique name of the format to parse with
        :param type_to: The unique name of the format to compose with
        :param data: The text to convert
        """
        try:
            return self.compose(type_to, self.parse(type_from, data))
        except Exception as e:
            raise ValueError(
                "Couldn't convert '{from_}' to '{to}'. Possibly "
                "because the parser of '{from_}' generates a "
                "data structure incompatible with the composer "
                "of '{to}'. This is the original error: \n\n"
                "{error}: {message}".format(from_=type_from, to=type_to,
                                            error=e.__class__.__name__,
                                            message=e.message))

    def meta(self, type):
        """Retreived meta information of a format.

        :param meta: The extra information associated with the format
        """
        try:
            return self.registered_formats[type].get('meta')
        except KeyError:
            raise NotImplementedError("No format registered with type "
                                      "'{type}'".format(type=type))

    def discover(self, exclude=None):
        """Automatically discovers and registers installed formats.

        If a format is already registered with an exact same name, the
        discovered format will not be registered.

        :param exclude: (optional) Exclude formats from registering
        """
        if exclude is None:
            exclude = []
        elif not isinstance(exclude, (list, tuple)):
            exclude = [exclude]

        if 'json' not in exclude and 'json' not in self.registered_formats:
            self.discover_json()
        if 'yaml' not in exclude and 'yaml' not in self.registered_formats:
            self.discover_yaml()

    def discover_json(self):
        """Discovers the JSON format and registers it if available.

        To speed up JSON parsing and composing, install `simplejson`::

            pip install simplejson

        The standard library module `json` will be used by default.
        """
        try:
            import simplejson as json
        except ImportError:
            import json
        self.register('json', json.loads, json.dumps)

    def discover_yaml(self):
        """Discovers the YAML format and registers it if available.

        Install YAML support via PIP::

            pip install PyYAML
        """
        try:
            import yaml
            self.register('yaml', yaml.load, yaml.dump)
        except ImportError:
            pass
