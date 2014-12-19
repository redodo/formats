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

    def register(self, type, parser, composer):
        """Registers a parser and composer of a format.

        You can use this method to overwrite existing formats.

        :param type: The unique name of the format
        :param parser: The method to parse data as the format
        :param composer: The method to compose data as the format
        """
        self.registered_formats[type] = {
            'parser': parser,
            'composer': composer,
        }

    def register_parser(self, type, parser):
        """Registers a parser of a format.

        :param type: The unique name of the format
        :param parser: The method to parse data as the format
        """
        try:
            self.registered_formats[type]['parser'] = parser
        except KeyError:
            self.registered_formats[type] = {'parser': parser}

    def register_composer(self, type, composer):
        """Registers a composer of a format.

        :param type: The unique name of the format
        :param composer: The method to compose data as the format
        """
        try:
            self.registered_formats[type]['composer'] = composer
        except KeyError:
            self.registered_formats[type] = {'composer': composer}

    def parser(self, type):
        """Registers the decorated method as the parser of a format.

        :param type: The unique name of the format
        """
        def decorator(f):
            self.register_parser(type, f)
            return f
        return decorator

    def composer(self, type):
        """Registers the decorated method as the composer of a format.

        :param type: The unique name of the format
        """
        def decorator(f):
            self.register_composer(type, f)
            return f
        return decorator

    def parse(self, type, text):
        """Parse text as a format.

        :param type: The unique name of the format
        :param text: The text to parse as the format
        """
        try:
            return self.registered_formats[type]['parser'](text)
        except KeyError:
            raise NotImplementedError("No parser found for "
                                      "type '{}'".format(type))

    def compose(self, type, text):
        """Compose text as a format.

        :param type: The unique name of the format
        :param text: The text to compose as the format
        """
        try:
            return self.registered_formats[type]['composer'](text)
        except KeyError:
            raise NotImplementedError("No composer found for "
                                      "type '{}'".format(type))

    def convert(self, type_from, type_to, text):
        """Parsers data from with one format and composes with another.

        :param type_from: The unique name of the format to parse with
        :param type_to: The unique name of the format to compose with
        :param text: The text to convert
        """
        return self.compose(type_to, self.parse(type_from, text))

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
            try:
                import simplejson as json
            except ImportError:
                import json
            self.register('json', json.loads, json.dumps)

        if 'yaml' not in exclude and 'yaml' not in self.registered_formats:
            try:
                import yaml
                # from yaml import Loader, SafeLoader
                #
                # def construct_yaml_str(self, node):
                #     # Override the default string handling function
                #     # to always return unicode objects
                #     return self.construct_scalar(node)
                # Loader.add_constructor(u'tag:yaml.org,2002:str', construct_yaml_str)
                # SafeLoader.add_constructor(u'tag:yaml.org,2002:str', construct_yaml_str)

                self.register('yaml', yaml.load, yaml.dump)
            except ImportError:
                pass
