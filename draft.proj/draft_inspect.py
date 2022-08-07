import dependencies
# python
import inspect
from abc import ABC, abstractmethod
from typing import Any, Dict, Tuple, Type
# 3rd party
from nameof import nameof
# project
from fastdi.injection.validation import validate_registration, validate_constructor


class IStringProvider(ABC):
    @abstractmethod
    def provide_str(self) -> str:
        raise NotImplementedError()
    
    
    @abstractmethod
    def place_str(
        self, 
        data : list
    ) -> None:
        raise NotImplementedError()


    @abstractmethod
    def __repr__(self) -> str:
        raise NotImplementedError()



class IIntProvider(ABC):
    @abstractmethod
    def provide_int(self) -> int:
        raise NotImplementedError()


    @abstractmethod
    def __len__(self):
        raise NotImplementedError()



class ValueStringProvider(IStringProvider, IIntProvider):
    def __init__(self, value : str, data : int):
        self.value = value


    def provide_str(self) -> str:
        return f'{self.value}'
    
    
    def place_str(
        self, 
        data : list
    ) -> None:
        data[0] = self.value

    
    def provide_int(self) -> str:
        return self.value


    def __len__(self):
        return 1


    def __repr__(self) -> str:
        return f'{self.value}'
    
    
    def is_int(self):
        return True


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    
if __name__ == '__main__':
    vsp = ValueStringProvider(153, 1)

    val = vsp.provide_str()

    validate_registration(IStringProvider, ValueStringProvider)
    
    validate_constructor(ValueStringProvider)