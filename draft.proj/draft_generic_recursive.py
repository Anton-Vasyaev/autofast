# python
from abc import abstractclassmethod, ABC
from typing import Generic, TypeVar
# 3rd party
import numpy as np
# project
from autofast.reflection.meta import get_class_meta_info
from auxiliary              import print_class_meta_info 


T = TypeVar('T')
V = TypeVar('V')
K = TypeVar('K')

ProvideT = TypeVar('ProvideT')
RefT     = TypeVar('RefT')

class AlgTuple2(Generic[T]):
    v1 : T

    v2 : T

    def __init__(self, v1 : T, v2 : T):
        ''''''
        self.v1 = v1
        self.v2 = v2


class Ref(Generic[T]):
    pass


class RefHandler(Generic[RefT]):
    pass


class IDataProvider(ABC, Generic[T]):
    @abstractclassmethod
    def provide_data(self, idx : int) -> T:
        raise NotImplementedError()
    

class ProviderPool(ABC, Generic[ProvideT]):
    @abstractclassmethod
    def get_provider(self) -> ProvideT:
        raise NotImplementedError()


class DataProviderPool(ProviderPool[IDataProvider[T]], AlgTuple2[int]):
    def get_provider(self) -> IDataProvider[T]:
        pass


class IntDataProviderPool(DataProviderPool[RefHandler[Ref[int]]]):
    def get_provider(self) -> IDataProvider[RefHandler[Ref[int]]]:
        pass


if __name__ == '__main__':
    t = IntDataProviderPool

    cls_info = get_class_meta_info(t)

    print_class_meta_info(cls_info)