# python
from dataclasses import dataclass
# project
from .city_data  import CityData
from .mayor_data import MayorData


@dataclass
class CityMessage:
    city  : CityData
    mayor : MayorData