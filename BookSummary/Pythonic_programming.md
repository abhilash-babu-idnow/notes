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

