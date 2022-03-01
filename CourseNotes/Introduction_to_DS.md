# Week 2
### Querying a DataFrame
For some data frame with a column name say col1 the following are equivalent
```python
df[df['col1'] > 10]
```

and 

```python
col1_mask = df['col1'] > 10
df.where(col1_mask).dropna()
```

- Use the  `&`  and  `|`  operator to AND and OR the binary masks 
- Can chain operations like

``` python
df[df['col1'].gt(10).lt(40)]
```

### Indexing Dataframes
- Use `set_index`  to set a column as index. 
- Multilevel index can be created by passing a list of column names to  `set_index`  function.

# Week 4
## Basic Statistical Testing
- Statistical testing in python
- Hypothesis testing
- Statistical significance
- Scipy to run student's t-tests

```python

import numpy as np
import pandas as pd
from scipy import stats

```

- Statistical properties of two populations - are they similar or different. 
	- Alternative hypothesis - These are different
	- Null hypothesis - These are the same.
	- In the lecture, we looked at the the mean of the assignment grade of the students who submitted the assignment early and who submitted the assignment late. The mean value was almost the same around 75. So does that mean that these two populations are statistically similar? This is where the student t-test comes in. It tests the alternative and null hypothesis. 
	- use ttest_ind - independent t-tests