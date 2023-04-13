# python
from dataclasses import dataclass
# project
from autofast.config import field_meta



@dataclass
class MayorConfiguration:
    name : str

    age : int
    
    skills : float
    