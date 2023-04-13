# python
from abc import abstractclassmethod
# project
from ..data import CityData


class ICityProvider:
    @abstractclassmethod
    def provide_city(self) -> CityData:
        raise NotImplementedError()