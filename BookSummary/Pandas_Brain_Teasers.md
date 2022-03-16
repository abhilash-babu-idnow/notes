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

- Puzzle 10

What is the answer?

```python

```