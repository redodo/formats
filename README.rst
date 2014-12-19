Formats
=======

|Version| |License|

.. |Version| image:: https://img.shields.io/pypi/v/formats.svg?style=flat
    :target: https://pypi.python.org/pypi/formats
    :alt: Version
.. |License| image:: https://img.shields.io/pypi/l/formats.svg?style=flat
    :target: https://github.com/redodo/formats/blob/master/LICENSE
    :alt: License


Installation via PIP::

    pip install --pre formats


Quick usage overview::

    >>> import formats
    >>> formats.discover()
    >>> text = '''
    ...     awesome_things:
    ...     - dodos
    ...     - pythons
    ... '''
    >>> formats.parse('yaml', text)
    {'awesome_things': ['dodos', 'pythons']}
    >>> formats.convert('yaml', 'json', text)
    '{"awesome_things": ["dodos", "pythons"]}'
