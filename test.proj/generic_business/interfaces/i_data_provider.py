# python
from abc import abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')

class IDataProvider(Generic[T]):
    @abstractmethod
    def provide_data(self) -> T:
        raise NotImplementedError()