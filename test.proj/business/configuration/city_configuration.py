# python
from dataclasses import dataclass
# project
from autofast.config import field_meta



@dataclass
class CityConfiguration:
    name       : str = field_meta(required=True)
    population : int = field_meta(required=True)