# python
from abc import ABC, abstractmethod
# project
from ..data import CityMessage


class IMessageFormatter(ABC):
    @abstractmethod
    def format_message(self, message : CityMessage) -> str:
        raise NotImplementedError()