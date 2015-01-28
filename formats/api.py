# -*- coding: utf-8 -*-

from .banks import FormatBank


#: API methods will be executed on the default format bank.
default_bank = FormatBank()


def bank(discover=False, exclude=None):
    """Creates a new `FormatBank` object and optionally discovers
    installed formats.

    :param discover: (optional) When ``True``, formats are
        automatically discovered
    :param exclude: (optional) Exclude formats from being discovered.
    """
    return FormatBank(discover, exclude)


def register(type, parser, composer, **meta):
    """Registers a parser and composer of a format.

    You can use this method to overwrite existing formats.

    :param type: The unique name of the format
    :param parser: The method to parse data as the format
    :param composer: The method to compose data as the format
    :param meta: The extra information associated with the format
    """
    return default_bank.register(type, parser, composer, **meta)


def register_parser(type, parser, **meta):
    """Registers a parser of a format.

    :param type: The unique name of the format
    :param parser: The method to parse data as the format
    :param meta: The extra information associated with the format
    """
    return default_bank.register_parser(type, parser, **meta)


def register_composer(type, composer, **meta):
    """Registers a composer of a format.

    :param type: The unique name of the format
    :param composer: The method to compose data as the format
    :param meta: The extra information associated with the format
    """
    return default_bank.register_composer(type, composer, **meta)


def parser(type, **meta):
    """Registers the decorated method as the parser of a format.

    :param type: The unique name of the format
    :param meta: The extra information associated with the format
    """
    return default_bank.parser(type, **meta)


def composer(type, **meta):
    """Registers the decorated method as the composer of a format.

    :param type: The unique name of the format
    :param meta: The extra information associated with the format
    """
    return default_bank.composer(type, **meta)


def parse(type, data):
    """Parse text as a format.

    :param type: The unique name of the format
    :param data: The text to parse as the format
    """
    return default_bank.parse(type, data)


def compose(type, data):
    """Compose text as a format.

    :param type: The unique name of the format
    :param data: The text to compose as the format
    """
    return default_bank.compose(type, data)


def convert(type_from, type_to, data):
    """Parsers data from with one format and composes with another.

    :param type_from: The unique name of the format to parse with
    :param type_to: The unique name of the format to compose with
    :param data: The text to convert
    """
    return default_bank.convert(type_from, type_to, data)


def meta(type):
    """Retreived meta information of a format.

    :param meta: The extra information associated with the format
    """
    return default_bank.meta(type)


def discover(exclude=None):
    """Automatically discovers and registers installed formats.

    If a format is already registered with an exact same name, the
    discovered format will not be registered.

    :param exclude: (optional) Exclude formats from registering
    """
    return default_bank.discover(exclude)
