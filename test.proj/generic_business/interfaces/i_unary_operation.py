# python
from abc    import abstractmethod
from typing import Generic, TypeVar, Type


T = TypeVar('T')


class IUnaryOperation(Generic[T]):
    @abstractmethod
    def operate(self, data : T) -> T:
        raise NotImplementedError()


    def __call__(self, data : T) -> T:
        return self.operate(data)