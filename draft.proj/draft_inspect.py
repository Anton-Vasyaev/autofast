# python
import inspect
from abc import ABC, abstractmethod


class IStringProvider(ABC):
    @abstractmethod
    def provide_str(self) -> str:
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
    def __init__(self, value):
        self.value = value


    def provide_str(self) -> str:
        return f'{self.value}'

    
    def provide_int(self) -> str:
        return self.value


    def __len__(self):
        return 1


    def __repr__(self):
        return f'{self.value}'


def get_methods(data_type):
    methods = []
    for name in dir(data_type):
        data = getattr(data_type, name)
        print(f'data:{data}')
        if callable(data):
            methods.append(data)

    return methods

    #return [func for func in dir(data_type) if callable(getattr(data_type, func))]


def get_interface_methods(provide_type):
    methods_names = get_methods(provide_type)

    for method_name in methods_names:
        print(method_name)
    


def validate_registration(provide_type, register_type):
    interface_methods = get_interface_methods(provide_type)



    



if __name__ == '__main__':
    vsp = ValueStringProvider(153)

    val = vsp.provide_str()

    print(f'val:{val}')

    validate_registration(IStringProvider, vsp)