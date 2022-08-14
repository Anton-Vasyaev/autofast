from ..data.city_data import CityData
from ..data import MayorData

from  ..interfaces import ICityProvider



class RussianCityProvider(ICityProvider):
    def provide_city(self) -> MayorData:
        return CityData("cherepovets", 340521)