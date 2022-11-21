# python
from abc import abstractmethod
from typing import TypeVar, Generic

InT = TypeVar('InT')
OutT = TypeVar('OutT')


class IProcessor(Generic[InT, OutT]):
    @abstractmethod
    def process(self, data : InT) -> OutT:
        raise NotImplementedError()


    def __call__(self, data : InT) -> OutT:
        return self.process(data)