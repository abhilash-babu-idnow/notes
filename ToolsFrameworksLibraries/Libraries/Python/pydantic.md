% pydantic

#pydantic #data-validation #settings-management #python #library #python-package

### Resources

- [Documentation](https://pydantic-docs.helpmanual.io/)


### Notes

- What is pydantic?

> Data validation and settings management using python type annotations.


Example from the docs

```python
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    'id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3'],
}
user = User(**external_data)
```


