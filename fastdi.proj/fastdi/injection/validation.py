# python
import inspect
from dataclasses import dataclass
from typing      import Any, Dict
# 3rd party
from nameof import nameof
# project
from fastdi.reflection.function import *



@dataclass
class FunctionInfo:
    func_name         : str
    function_instance : Any
    args_info         : inspect.FullArgSpec
    is_abstract       : bool
    
    @staticmethod
    def from_function(function : Any):
        return FunctionInfo(
            get_function_short_name(function),
            function,
            inspect.getfullargspec(function),
            is_abstract_function(function)
        )
    
    
def get_functions_info(data_type : Type) -> Dict[str, FunctionInfo]:
    abstract_functions = {}

    functions = get_functions(data_type)
    for function in functions:
        short_name    = get_function_short_name(function)
        args          = inspect.getfullargspec(function)
        abstract_flag = is_abstract_function(function)
        abstract_functions[short_name] = FunctionInfo(short_name, function, args, abstract_flag)

    return abstract_functions


def get_signature_dict(provide_func_args : inspect.FullArgSpec) -> Dict[str, Any]:
    signature_dict = {
        'return' : ''
    }
    
    annotations = provide_func_args.annotations
    
    for arg_name in provide_func_args.args:
        arg_anno = ''
        if arg_name in annotations:
            arg_anno = annotations[arg_name]
            
        signature_dict[arg_name] = arg_anno
    
    if 'return' in annotations:
        signature_dict['return'] = annotations['return']
        
    return signature_dict


def get_func_info_str_present(func_info : FunctionInfo) -> str:
    string_list = []
    string_list.append(f'{func_info.func_name}(')
    
    args       = func_info.args_info.args
    annotation = func_info.args_info.annotations
    
    for arg_idx in range(len(args)):
        arg = args[arg_idx]
        string_list.append(arg)
        if arg in annotation:
            arg_anno = annotation[arg]
            string_list.append(f' : {arg_anno}')
            
        if arg_idx != len(args) - 1:
            string_list.append(', ')
    
    string_list.append(')')
    
    if 'return' in annotation:
        return_anno = annotation['return']
        
        string_list.append(f' -> {return_anno}')


    return ''.join([s for s in string_list])


def validate_functions_signatures(
    provide_type       : Type,
    register_type      : Type,
    provide_func_info  : FunctionInfo,
    register_func_info : FunctionInfo
) -> None:
    provide_signatures  = get_signature_dict(provide_func_info.args_info)
    register_signatures = get_signature_dict(register_func_info.args_info)
    
    func_name = provide_func_info.func_name
    
    if provide_signatures != register_signatures:
        raise ValueError(
            f'Signatures do not match of function \'{func_name}\' '
            f'in {nameof(provide_type)} \'{provide_type}\' and '
            f'{nameof(register_type)} \'{register_type}: '
            f'{get_func_info_str_present(provide_func_info)} != '
            f'{get_func_info_str_present(register_func_info)}.'
        )



def validate_same_functions(
    provide_type  : Type,
    register_type : Type
) -> None:
    provide_functions  = get_functions_info(provide_type)
    register_functions = get_functions_info(register_type)

    for provide_func_name, provide_func_info in provide_functions.items():
        if not is_abstract_function(provide_func_info.function_instance): continue

        if not provide_func_name in register_functions:
            raise ValueError(
                f'Abstract function \'{provide_func_name}\' from ' 
                f'abstract class \'{provide_type}\' '
                f'not implemented in \'{register_type}\'.'
            )

        register_func_info = register_functions[provide_func_name]

        validate_functions_signatures(
            provide_type,
            register_type,
            provide_func_info,
            register_func_info
        )


def validate_registration(provide_type, register_type, strong_abstract = False):
    if provide_type is register_type:
        return

    if not issubclass(register_type, provide_type):
        raise ValueError(
            f'Invalid registration \'{register_type}\' as \'{provide_type}\', '
            f'because {register_type} is not inherited from {provide_type}.'
        )
    
    if not strong_abstract:
        return

    if not inspect.isabstract(provide_type):
        raise ValueError(
            f'Invalid registration \'{register_type}\' as \'{provide_type}\', '
            f'because {nameof(provide_type)} is not abstract.'
        )
    
    validate_same_functions(provide_type, register_type)
    
    
def validate_constructor(data_type: Type):
    if not '__init__' in dir(data_type):
        raise ValueError(f'\'{data_type}\' has not constructor function \'__init__\'')

    init_func = getattr(data_type, '__init__')

    args_info = inspect.getfullargspec(init_func)
    
    if len(args_info.args) <= 1:
        return
    
    for arg_name in args_info.args[1:]:
        if not arg_name in args_info.annotations:
            raise ValueError(
                f'argument \'{arg_name}\' has not annotation in constructor function \'__init__\' '
                f'of type \'{data_type}\''
            )