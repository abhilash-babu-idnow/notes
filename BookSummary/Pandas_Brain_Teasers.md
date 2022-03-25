- Puzzle 1

What is the output?

```python
import pandas as pd

def relu(n):
	if n < 0: 
		return 0
	return n

arr = pd.Series([-1, 0, 1])
print(relu(arr))
```

---

Answer: Value Error. 

Pandas series / dataframe  - Truth value is ambiguous. Use ``` a.empty() a.bool() a.item() a.any() a.all()```  etc 

```python
import numpy as np

@np.vectorize
def relu(n):
	if n < 0: 
		return 0
	return n

```

> A _ufunc_ (Universal function) works with both scalars, numpy arrays and pandas

---

- Puzzle 2

What is the output?

```python
import pandas as pd

simpsons = pd.Series(['Homer', 'Marge', 'Lisa', 'Maggie'])

print('Bart' in simpsons)
```

---

Answer: False

Pandas series acts like a dict with index as the key and values as values of a dict. So inorder to make this work we will have to use 

```python
print('Bart' in simpsons.values)
```

---

- Puzzle 3

What is the output?

```python
from io import StringIO
import pandas as pd

csv_data = '''\
day, hits
2020-01-01, 400
2020-02-02, 600
2020-02-03, 500
'''

df = pd.read_csv(StringIO(csv_data))
print(df.day.dt.month.unique())
```

---

Answer: Attribute Error.

pandas doesn't know that the column has a date type. We will have to convert the type manually or use the parameter parse_dates in read_csv function

```python
df = pd.read_csv(StringIO(csv_data), parse_dates=['day'])
```


---

- Puzzle 9

What is the answer?

```python
import pandas as pd

grades = pd.Series([61, 82, 57])
bonuses = pd.Series([10, 5, 10, 10])
out = grades + bonuses

print(out)
```

---

Answer: 71, 87, 67, NaN
This behaviour is different from that of numpy. Numpy will not be able to broadcast and throw and Value Error. On the otherhand when pandas can't find a maching index it will use __nan__ for a value.

---

- Puzzle 10 - Free Range

What is the answer?

```python
import pandas as pd

nums = pd.Series([1, 2, 3, 4, 5, 6])
print(nums[(nums > 2) and  (nums < 5)])
```

---


Answer : Value Error

`and` is invoked on two Boolean series and that raises an error. So use 

- `&`  instead of `and` 
- `|` instead of `or`
- `~` instead of `not`

---

- Puzzle 11 - Phil? Nah!?

What is the answer?

```python
import pandas as pd
import numpy as np

s = pd.Series([1, 2, np.nan, 4, 5])
s.fillna(3)
print(s.sum())
```

---

Answer: 12.0

__fillna__ returns a new series unless the parameter __inplace__ is set to __True__


---

- Puzzle 12 - Multiplying

What is the answer?

```python
import pandas as pd

v = pd.Series([0.1, 1.0, 1.1])
out = v * v
expected = pd.Series([0.01, 1.0, 1.2])
if (out == expected).all():
	print("Math rocks")
else:
	print("Please reinstall universe and reboot")
```

---

Aswer: Please reinstall universe and reboot.

Floating point comparison!

use `numpy.allclose` instead

---

- Puzzle 13 - 10% discout

What is the answer

```python
import pandas as pd

df = pd.DataFrame([
	['Bugs', True, 72.1],
	['Daffy', False, 30.7],
	['Tweety', True, 23.5],
	['Elmer', False, 103.9]
], columns=['Customer', 'Member', 'Amount'])

df[df['Member']]['Amount'] *= 0.9
print(df)
```

---

Answer:
Warning and df is not updated 

Reason: pandas tries to avoid copying of data. It is returning a view.

Solution:

```python
df.loc[df['Member'], 'Amount'] *= 0.9
```

---

- Puzzle 14 - A tale of one city

What is the answer?

```python
import pandas as pd

cities = pd.DataFrame([
	('Vienna', 'Austria', 1_899_055),
	('Sofia', 'Bulgaria', 1_238_438),
	('Tekirdag', 'Turkey', 1_055_412),
	], columns=['City', 'Country', 'Population']
)

```