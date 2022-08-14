from ..data          import CityData, MayorData
from ..configuration import CityConfiguration
from ..interfaces    import ICityProvider



class ConfigCityProvider(ICityProvider):
    def __init__(
        self,
        config : CityConfiguration
    ):
        self.config = config
        
    
    def provide_city(self) -> MayorData:
        return CityData(self.config.name, self.config.population)