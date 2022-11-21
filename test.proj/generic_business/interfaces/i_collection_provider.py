# python
from abc import abstractmethod
from typing import TypeVar, Generic, List

T = TypeVar('T')

class ICollectionProvider(Generic[T]):
    @abstractmethod
    def provide_collection(self) -> List[T]:
        raise NotImplementedError()