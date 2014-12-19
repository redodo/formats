# -*- coding: utf-8 -*-
"""
    Formats
    ~~~~~~~

    Support multiple formats with ease.

    :copyright: (c) 2014 by Hidde Bultsma.
    :license: MIT, see LICENSE for more details.
"""

from .api import (
    default_bank, bank, register, register_parser, register_composer,
    parser, composer, parse, compose, convert, discover
)
from .banks import FormatBank
