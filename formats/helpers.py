# -*- coding: utf-8 -*-


from .api import default_bank


def discover_json(bank=None, **meta):
    """Discovers the JSON format and registers it if available.

    To speed up JSON parsing and composing, install `simplejson`::

        pip install simplejson

    The standard library module `json` will be used by default.

    :param bank: The format bank to register the format in
    :param meta: Extra information associated with the format
    """
    try:
        import simplejson as json
    except ImportError:
        import json
    if bank is None:
        bank = default_bank
    bank.register('json', json.loads, json.dumps, **meta)


def discover_yaml(bank=None, **meta):
    """Discovers the YAML format and registers it if available.

    Install YAML support via PIP::

        pip install PyYAML

    :param bank: The format bank to register the format in
    :param meta: Extra information associated with the format
    """
    try:
        import yaml
        if bank is None:
            bank = default_bank
        bank.register('yaml', yaml.load, yaml.dump, **meta)
    except ImportError:
        pass
