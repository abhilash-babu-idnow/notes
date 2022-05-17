% Enums

```python
from enum import Enum

class Player(Enum):
	Batsman = 0
	Bowler  = 1
	WicketKeeper = 2
```

- unique decorator ? #unique #python #enum

> `enum.``unique`()
> Enum class decorator that ensures only one name is bound to any one value.

[Ensuring unique enumeration values](https://docs.python.org/3/library/enum.html#ensuring-unique-enumeration-values "Permalink to this headline")

By default, enumerations allow multiple names as aliases for the same value. When this behavior isn’t desired, the following decorator can be used to ensure each value is used only once in the enumeration:

``` python
>>> from enum import Enum, unique
>>> @unique
... class Mistake(Enum):
...     ONE = 1
...     TWO = 2
...     THREE = 3
...     FOUR = 3
...
Traceback (most recent call last):
...
ValueError: duplicate values found in <enum 'Mistake'>: FOUR -> THREE
```