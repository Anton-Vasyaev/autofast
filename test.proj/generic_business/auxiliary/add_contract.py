# python
from typing import TypeVar, Protocol, runtime_checkable
from abc import abstractmethod

T_co = TypeVar('T_co', covariant=True)

@runtime_checkable
class SupportsAdd(Protocol[T_co]):
    @abstractmethod
    def __add__(self, x : T_co) -> T_co: ...