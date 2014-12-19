Formats
=======

[<img src="https://img.shields.io/pypi/v/formats.svg?style=flat">](https://pypi.python.org/pypi/formats)
[<img src="https://img.shields.io/pypi/l/formats.svg?style=flat">](https://github.com/redodo/formats/blob/master/LICENSE)

*Support multiple formats with ease.*


Installation via PIP:

```bash
pip install --pre formats
```


Quick usage overview:

```python
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
```


The Basics
----------

Formats will provide you with a consistent API to parse and compose
data.


Registering new formats
-----------------------

```python
import formats
import someformat

formats.register('someformat', someformat.loads, someformat.dumps)
# or
formats.register_parser('someformat', someformat.loads)
formats.register_composer('someformat', someformat.dumps)
```


Creating your own formats
-------------------------

You could of course use the `register` method to register your own
parser, but decorators are much more fun!

```python
import formats

@formats.parser('text')
def text_parser(text):
    return text

@formats.composer('text')
def text_composer(text):
    return text
```
