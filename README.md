# EZDict

Making Python's `dict` easier to work with by adding object notation and grouping.
 1. Allows keys to be accessed as attributes, so `ezdict.attr` can be used instead of 
 `ezdict["attr"]`. Note, this only works with string keys. Additionally, any
 keys that overlap with method names will be shadowed, so to access the key `keys`,
 use `ezdict["keys"]` instead of `ezdict.keys`.
 2. Provide two methods, `incrementer` and `appender`, to support the common operations
 of counting the occurrences of a key and grouping values by a key, respectively.

## Installation

```
pip install ezdict
```

## Import

```python
from ezdict import EZDict
```

## Usage

### Accessing Keys as Attributes

```python
from ezdict import EZDict

ez = EZDict({
    "id": "5e2797c05aa0585816ce8b8c",
    "title": "EZDict",
    "description": "Super cool Python package",
    "author": "Jacob Morris (BlendingJake)",
    "meta": {
        "created": "March 27th, 2020"
    }
})

print(ez.title)  # >>> "EZDict"
print(ez.meta.created)  # >>> "March 27th, 2020"
```

### Grouping/Counting Like a Pro
```python
from ezdict import EZDict

# tried of this?
iterable = [ ... ]
grouped = {}
for item in iterable:
    if item["key"] in grouped:
        grouped[item["key"]] += 1
        # OR grouped[item["key"]].append(item)
    else:
        grouped[item["key"]] = 1
        # OR grouped[item["key"]] = [item]

# do this instead
iterable = [ ... ]
grouped = EZDict()
for item in iterable:
    grouped.incrementer(item["key"])
    # OR grouped.appender(item["key"], item)
```

#### `incrementer(key, increment=1)`

>Increment `key` by `increment` if the key has already been seen. Otherwise,
>set the key equal to `increment`.


#### `appender(key, value)`

>Append `value` to the list of values associated with `key` if that key was
>already been seen. Otherwise, set the key equal to `[value]`.