# python
import inspect
from typing import List, Type, Any



def get_functions(data_type : Type) -> List[Any]:
    functions = []
    for name in dir(data_type):
        data = getattr(data_type, name)
        if inspect.isfunction(data):
            functions.append(data)

    return functions


def is_abstract_function(function_type : Any) -> bool:
    if hasattr(function_type, '__isabstractmethod__'):
        return True


def get_function_short_name(function) -> str:
    func_name : str = getattr(function, '__qualname__')
    
    return func_name.split('.')[1]