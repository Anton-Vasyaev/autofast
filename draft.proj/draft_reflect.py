import dependencies
# python
from typing import Optional, List, Tuple, Union
from dataclasses import dataclass
# 3rd party
import autofast.reflection.generic as reflect_generic 


@dataclass
class Point:
    x : float
    y : float


a = Union[List[int], None]

b = Tuple[int, float]

c = Optional[Point]

print(reflect_generic.is_optional(a))
print(reflect_generic.is_optional(b))
print(reflect_generic.is_optional(c))

print(reflect_generic.get_optional_type(a))
print(reflect_generic.get_optional_type(c))