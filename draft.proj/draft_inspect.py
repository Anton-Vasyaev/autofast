# python
from dataclasses import dataclass
import inspect
from abc import ABC, abstractmethod
from typing import Any, Dict, Type
# 3rd party
from nameof import nameof


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
    def __init__(self, value):
        self.value = value


    def provide_str(self) -> str:
        return f'{self.value}'
    
    
    def place_str(
        self, 
        data : list,
        mirror : float
    ) -> None:
        data[0] = self.value

    
    def provide_int(self) -> str:
        return self.value


    def __len__(self):
        return 1


    def __repr__(self):
        return f'{self.value}'
    
    
    def is_int(self):
        return True


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def get_functions(data_type):
    functions = []
    for name in dir(data_type):
        data = getattr(data_type, name)
        if inspect.isfunction(data):
            functions.append(data)

    return functions


def is_abstract_function(function_type):
    if hasattr(function_type, '__isabstractmethod__'):
        return True


def get_short_function_name(function):
    return getattr(function, '__qualname__').split('.')[1]



@dataclass
class FunctionInfo:
    function_instance : Any
    args_info         : inspect.FullArgSpec
    is_abstract       : bool



def get_functions_info(data_type : Type) -> Dict[str, FunctionInfo]:
    abstract_functions = {}

    functions = get_functions(data_type)
    for function in functions:
        short_name    = get_short_function_name(function)
        args          = inspect.getfullargspec(function)
        abstract_flag = is_abstract_function(function)

        abstract_functions[short_name] = FunctionInfo(function, args, abstract_flag)

    return abstract_functions


def validate_function_args(
    provide_type,
    register_type,
    provide_args_info,
    register_args_info
):
    pass


def validate_same_functions(
    provide_type,
    register_type
):
    provide_functions  = get_functions_info(provide_type)
    register_functions = get_functions_info(register_type)

    for provide_func_name, provide_func_info in provide_functions.items():
        if not is_abstract_function(provide_func_info.function_instance): continue

        print(type(provide_func_info.function_instance))

        if not provide_func_name in register_functions:
            raise ValueError(
                f'Abstract function \'{provide_func_name}\' from ' 
                f'abstract class \'{provide_type}\' '
                f'not implementation in \'{register_type}\'.'
            )

        register_func_info = register_functions[provide_func_name]

        provide_args_spec  = provide_func_info.args_info
        register_args_spec = register_func_info.args_info

        provide_args = provide_args_spec.args
        register_args = register_args_spec.args
        if provide_args != register_args:
            raise ValueError(
                f'different args in function \'{provide_func_name} in '
                f'{nameof(provide_type)} \'{provide_type}\' and {nameof(register_type)} \'{register_type}\':'
                f'{provide_args} != {register_args}'
            )
        print(provide_func_info.args_info)



    


def validate_registration(provide_type, register_type, strong_abstract = False):
    if provide_type is register_type:
        return

    if not issubclass(register_type, provide_type):
        raise ValueError(
            f'Invalid registration \'{register_type}\' as \'{provide_type}\', '
            f'because {register_type} is not inherited from {provide_type}.'
        )
    
    if not inspect.isabstract(provide_type) and not strong_abstract:
        return
    
    if not inspect.isabstract(provide_type):
        raise ValueError(
            f'Invalid registration \'{register_type}\' as \'{provide_type}\', '
            f'because {nameof(provide_type)} is not abstract.'
        )
    
    validate_same_functions(provide_type, register_type)    


    
if __name__ == '__main__':
    vsp = ValueStringProvider(153)

    val = vsp.provide_str()

    validate_registration(IStringProvider, ValueStringProvider)
    