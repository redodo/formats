# -*- coding: utf-8 -*-


class FormatBank(object):

    def __init__(self):
        self.registered_formats = {}

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
        try:
            return self.registered_formats[type]['composer'](text)
        except KeyError:
            raise NotImplementedError("No composer found for "
                                      "type '{}'".format(type))

    def convert(self, type_from, type_to, text):
        return self.compose(type_to, self.parse(type_from, text))

    def discover(self):
        import json
        self.register('json', json.loads, json.dumps)

