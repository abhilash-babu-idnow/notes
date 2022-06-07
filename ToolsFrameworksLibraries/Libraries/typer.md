% typer

- [Enum Choices](#enum-choices)

## Enum Choices
```python 
from enum import Enum

class Choices(Enum):
	a = "sachin"
	b = "sourav"
	c = "rahul"

def best_player(choice : Choices = typer.Argument(..., help="Player") -> None:
	print(f"Best player is {choice.value}")

if __name__ == "__main__":
	typer.run(best_player)
```

