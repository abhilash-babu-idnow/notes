Book: Effective Python 
Edition: 2nd
Started reading on: 13 March, 2022
Finished reading on : 

---

- Item 1 - Use python vesion 3
	- Check version using python --version or at runtime using
	
	```python
	import sys
	sys.version_info
	sys.version
	```

---

- Item 2 - Follow PEP 8 Style guide
	- Use pylint for automated enforcement of PEP8 style guide

---

- Item 3 - Know the difference between bytes and str
	- _bytes_ contains sequences of 8-bit values and _str_ contains Unicode characters
	- Use helper functions to convert to _bytes_ and _str_ 
	
		```python
		def to_bytes(s):
			return s.encode('utf-8')

		def to_str(b):
			return b.decode('utf-8')
		```

	- To read/write binary data from/to file use ```'rb' or 'wb'```

---
- Item 4 - Prefer Interpolated F-strings over c - style format strings and str.format

---

- Item 5 - Write helper functions instead of Complex Expressions.
	- it is tempting to use single line complex single line expressions but it makes it difficult to read. 
	- Move complex expressions to helper functions
	- Use if/else expression instead of _or_ and _and_ in expressions to make it more readable

---

- Item 6 - Prefer Multiple Assignment Unpacking Over Indexing.

```python
snacks = [('bacon', 350), ('donut', 240), ('muffin', 190)]
for rank, (name, calories) in enumerate(snacks, 1):
	print(f"#{rank} : {name} - {calories}")
```
