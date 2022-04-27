### Documenting tips
- ```import __hello__```  prints Hello World
- ```import this```  prints zen of python
- ```licence()```  prints license and ```credits()```  prints contributions

### General Tips
- Chain comparison operators  ```x<y>z```  implies x < y and y > z. 
- Expand the tabs 
- Pickle it
```python
with open('result.pkl', 'wb') as f:
	pickle.dump(python_obj, f)

with open('result.pkl', 'rb') as f:
	python_obj = pickle.load(f)
```


- Avoid range() in Loops
Use 
```python
for item in seq:
	do_something(item)
```

instead of 

```python
for i in range(len(seq)):
	do_something(seq[i])
```

- Pass it
- Try it
- Embrace comprehensions
- Make code compact with conditional expression

```python
value = x if cond else y
```



### Data structure tips
- Construct a single element tuple

```python
x = (0,)
```

Import thing is the __comma__ . Without the comma it will be an int

- 