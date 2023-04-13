# python
from abc import abstractmethod
# porject
from ..data import CityMessage



class IMessageLoader:
    @abstractmethod
    def load_message(self) -> CityMessage:
        raise NotImplementedError()