Title: Python Brain Teasers
Started Date: 15-03-2022

---

Puzzle 1: 

```python

class Player:
	count = 0

	def __init__(self):
		self.count += 1

p1 = Player()
print(Player.count)

```

---

Answer: 0

`self.count`  shadows the class variable `count`
So `p1.count` will be equal to `1`.

---

Puzzle 2:

``` python



```
