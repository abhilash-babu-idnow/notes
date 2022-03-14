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
