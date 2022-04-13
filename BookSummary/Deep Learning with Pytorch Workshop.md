an- Creating Tensors of Different Ranks using PyTorch

```python

import torch

t1 = torch.tensor([0.1, 1.0, 0.9, 0.3, 0.7])
t2 = torch.tensor([[0.1, 1.0, 0.9, 0.3, 0.7],
				  [0.2, 0.0, 0.3, 0.5, 0.4]])
t3 = torch.tensor([[[ 0.1, 0.3, 0.4, 0.8, 0.6],
					[ 0.3, 0.4, 0.5, 0.2, 0.1]],
				   [[ 0.1, 0.3, 0.4, 0.8, 0.6],
				     0.1, 0.3, 0.4, 0.8, 0.6]]])
```

