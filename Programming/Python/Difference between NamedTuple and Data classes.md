[Raymond Hettlinger's Pycon talk](https://www.youtube.com/watch?v=T-TwcmT6Rcw&t=1390)

| NamedTuple | DataClass |
|--------------|------------|
| Immutable | Mutable <sup>1<sup> |
| Inheritance is not easy |  Subclassing a dataclass is same as normal class |
| Based on Tuple | Based on Dict |

[1] Dataclasses can be made mutable by setting the frozen value to True