import dependencies
# python
from typing import TypeVar, Generic
from abc import ABC, abstractmethod
# project
from fastdi.reflection.data import ClassMetaInfo
from fastdi.reflection.meta import get_class_meta_info

from auxiliary import print_class_meta_info

T = TypeVar('T')
V = TypeVar('V')
K = TypeVar('K')



class DataPrinter(ABC, Generic[T]):
    @abstractmethod
    def print_data(self):
        raise NotImplementedError()


class DataProvider(DataPrinter[T], ABC):
    @abstractmethod
    def provide_data(self) -> T:
        raise NotImplementedError()


    def print_data(self):
        print(self.provide_data())


class DataAccumulator(DataProvider[T], ABC):
    @abstractmethod
    def accumulate_data(self, data : T):
        raise NotImplementedError()


class StringHandler(DataAccumulator[str], DataPrinter[str]):
    data : str

    def __init__(self, data : str):
        self.data = data


    def provide_data(self) -> str:
        return self.data

    
    def accumulate_data(self, data : str):
        self.data += data



if __name__ == '__main__':
    cls_info = get_class_meta_info(StringHandler)

    print_class_meta_info(cls_info)