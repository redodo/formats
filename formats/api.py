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


def register(type, parser, composer):
    """Registers a parser and composer of a format.

    You can use this method to overwrite existing formats.

    :param type: The unique name of the format
    :param parser: The method to parse data as the format
    :param composer: The method to compose data as the format
    """
    return default_bank.register(type, parser, composer)


def register_parser(type, parser):
    """Registers a parser of a format.

    :param type: The unique name of the format
    :param parser: The method to parse data as the format
    """
    return default_bank.register_parser(type, parser)


def register_composer(type, composer):
    """Registers a composer of a format.

    :param type: The unique name of the format
    :param composer: The method to compose data as the format
    """
    return default_bank.register_composer(type, composer)


def parser(type):
    """Registers the decorated method as the parser of a format.

    :param type: The unique name of the format
    """
    return default_bank.parser(type)


def composer(type):
    """Registers the decorated method as the composer of a format.

    :param type: The unique name of the format
    """
    return default_bank.composer(type)


def parse(type, text):
    """Parse text as a format.

    :param type: The unique name of the format
    :param text: The text to parse as the format
    """
    return default_bank.parse(type, text)


def compose(type, text):
    """Compose text as a format.

    :param type: The unique name of the format
    :param text: The text to compose as the format
    """
    return default_bank.compose(type, text)


def convert(type_from, type_to, text):
    """Parsers data from with one format and composes with another.

    :param type_from: The unique name of the format to parse with
    :param type_to: The unique name of the format to compose with
    :param text: The text to convert
    """
    return default_bank.convert(type_from, type_to, text)


def discover(exclude=None):
    """Automatically discovers and registers installed formats.

    If a format is already registered with an exact same name, the
    discovered format will not be registered.

    :param exclude: (optional) Exclude formats from registering
    """
    return default_bank.discover(exclude)
