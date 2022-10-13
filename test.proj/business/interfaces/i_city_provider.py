# python
from abc import ABC, abstractclassmethod
# project
from ..data import CityData


class ICityProvider(ABC):
    @abstractclassmethod
    def provide_city(self) -> CityData:
        raise NotImplementedError()