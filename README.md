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
