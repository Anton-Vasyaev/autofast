# python
from abc import ABC, abstractmethod
# porject
from ..data import CityMessage



class IMessageLoader(ABC):
    @abstractmethod
    def load_message(self) -> CityMessage:
        raise NotImplementedError()