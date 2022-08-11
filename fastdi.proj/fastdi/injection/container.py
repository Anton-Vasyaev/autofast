# python
import inspect
from typing import Any, Callable, Generic, List, Type
from dataclasses import dataclass
from enum import Enum, auto
# 3rd party
from nameof import nameof
# project
import fastdi.verify as fdi_ver

from .validation import validate_constructor, validate_registration


@dataclass
class ContainerOptions:
    strong_abstract : bool = True
    

class ResolveType(Enum):
    Instance  = auto()
    Singleton = auto()


class Container:
    def __init__(
        self, 
        container_options : ContainerOptions = ContainerOptions()
    ):
        fdi_ver.is_none(container_options, nameof(container_options))
        
        self.container_options = container_options
        
        self.config : dict = None
        
        self.registrations : List[_RegistrationPart] = {}
        
    
    def validate_registration(self, provide_type : Type, register_type : Type):
        validate_registration(
            provide_type,
            register_type,
            self.container_options.strong_abstract
        )
        

    def load_config(self, config : dict) -> None:
        self.config = config
    

    def register_type(
        self, 
        provide_type  : Type, 
        register_type : Type,
        resolve_type  : ResolveType
    ):
        validate_registration(
            provide_type, 
            register_type, 
            self.container_options.strong_abstract
        )
        
        validate_constructor(register_type)
        
        
        self.registrations[provide_type] = _RegistrationPart(
            provide_type,
            register_type,
            _TypeResolver(register_type),
            None,
            resolve_type
        )
        
        
    def register_factory(
        self,
        provide_type  : Type,
        register_type : Type,
        factory       : Callable[[Any], Any],
        resolve_type  : ResolveType
    ):
        validate_registration(
            provide_type,
            register_type,
            self.container_options.strong_abstract
        )
        
        self.registrations[provide_type] = _RegistrationPart(
            provide_type,
            register_type,
            factory,
            None,
            resolve_type
        )

        
        
    def resolve(self, data_type : Type) -> Any:
        if not data_type in self.registrations:
            raise ValueError(f'\'{data_type}\' is not registered.')
        
        reg_part = self.registrations[data_type]
        
        if reg_part.resolve_type == ResolveType.Singleton:
            if reg_part.instance is None:
                reg_part.instance = reg_part.factory(self)
                
            return reg_part.instance
        
        else:
            return reg_part.factory(self)
    

        
@dataclass
class _RegistrationPart:
    provide_type  : Type
    register_type : Type
    factory       : Callable[[Container], Any]
    instance      : Any
    resolve_type  : ResolveType



class _TypeResolver:
    def __init__(self, data_type : Type):
        self.data_type = data_type
        
        
    def __call__(self, container : Container) -> Type:
        init_func = getattr(self.data_type, '__init__')
        args_spec = inspect.getfullargspec(init_func)
        
        init_args = []
        
        for arg_name in args_spec.args[1:]:
            type = args_spec.annotations[arg_name]
            
            init_args.append((arg_name, type))
            
        build_args = { }
        for arg_name, arg_type in init_args:
            build_args[arg_name] = container.resolve(arg_type)
            
        return self.data_type(**build_args)