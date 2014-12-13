# -*- coding: utf-8 -*-

from .banks import FormatBank


__default_bank = FormatBank()


def register(type, parser, composer):
    return __default_bank.register(type, parser, composer)


def register_parser(type, parser):
    return __default_bank.register_parser(type, parser)


def register_composer(type, composer):
    return __default_bank.register_composer(type, composer)


def parser(type):
    return __default_bank.parser(type)


def composer(type):
    return __default_bank.composer(type)


def parse(type, text):
    return __default_bank.parse(type, text)


def compose(type, text):
    return __default_bank.compose(type, text)


def convert(type_from, type_to, text):
    return __default_bank.convert(type_from, type_to, text)


def discover():
    return __default_bank.discover()

