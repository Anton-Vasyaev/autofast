# python
from abc import abstractmethod
# project
from ..data import CityMessage


class IMessageFormatter:
    @abstractmethod
    def format_message(self, message : CityMessage) -> str:
        raise NotImplementedError()