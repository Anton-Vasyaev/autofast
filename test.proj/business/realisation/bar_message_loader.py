import dependencies
# project
import autofast.verify as fdi_ver 

from ..interfaces import IMessageLoader
from ..interfaces import ICityProvider
from ..interfaces import IMayorProvider
from ..data       import CityMessage



class BarMessageLoader(IMessageLoader):
    def __init__(
        self, 
        city_provider  : ICityProvider,
        mayor_provider : IMayorProvider
    ):
        self.city_provider  = city_provider
        self.mayor_provider = mayor_provider
    
    
    def load_message(self) -> CityMessage:
        city  = self.city_provider.provide_city()
        mayor = self.mayor_provider.provide_mayor()
        
        return CityMessage(city, mayor)
        