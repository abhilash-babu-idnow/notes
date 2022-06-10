% joblib

- Lightweight pipelining in python. 
	- transparent disk caching of functions
	
	```python
	from joblib import memory
	cachedir = 'your_cache_dir_goes_here'
	mem = Memory(cachedir)
	
	import numpy as np	
	a = np.vander(np.arange(3)).astype(float)
	square = mem.cache(np.square)
	
	b = square(a)
	c = square(a) # not evaluated value taken from cache
	```

	- lazy re-evaluation
	- parallel computing

