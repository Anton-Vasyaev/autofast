# python
from dataclasses import dataclass
# project
from fastdi.config import field_meta



@dataclass
class MayorConfiguration:
    name   : str   = field_meta(required=True)
    age    : int   = field_meta(required=True)
    skills : float = field_meta(required=True)
    