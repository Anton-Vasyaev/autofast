# python
from typing      import Type, Any, List
from dataclasses import dataclass
# project
from .function_meta_info import FunctionMetaInfo

@dataclass
class ClassMetaInfo:
    ''' Contains meta-information of class. '''

    type    : Type
    ''' Type. '''

    is_generic : bool
    ''' Flag indicating that class is generic. '''

    parents : List[Any]
    ''' Collection of meta-information of class parents. '''

    functions : List[FunctionMetaInfo]
    ''' Collection of meta-information of functions, defined in given class. '''