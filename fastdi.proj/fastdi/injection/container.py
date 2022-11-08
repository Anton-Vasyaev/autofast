from __future__ import annotations
# python
import inspect
from typing import Any, Callable, TypeVar, List, Type
from dataclasses import dataclass
from enum import Enum, auto
# 3rd party
from nameof import nameof
from ..config.data.configuration_options import ConfigurationOptions
# project
import fastdi.verify as fdi_ver

from .validation import validate_constructor, validate_registration
from ..config    import deserialize_config



_GenType = TypeVar('__GenType')



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
        
        self.config         : dict                 = None
        self.config_options : ConfigurationOptions = None
        
        self.registrations : List[_RegistrationPart] = {}
        
    
    def __validate_registration(self, provide_type : Type, register_type : Type):
        validate_registration(
            provide_type,
            register_type,
            self.container_options.strong_abstract
        )
        

    def load_config(
        self, 
        config  : dict,
        options : ConfigurationOptions = ConfigurationOptions()
    ):
        self.config         = config
        self.config_options = options
        
        
    def register_config(
        self, 
        config_type  : Type, 
        config_field : str
    ):
        if self.config is None:
            raise ValueError(f'Configuration is not loaded.')
            
        if not config_field in self.config:
            raise ValueError(f'Field \'{config_field}\' not present in configuration')
        
        self.registrations[config_type] = _RegistrationPart(
            config_type,
            config_type,
            _ConfigResolver(config_type, config_field),
            None,
            ResolveType.Singleton
        )
        

    def register_type(
        self, 
        provide_type  : Type, 
        register_type : Type,
        resolve_type  : ResolveType
    ):
        self.__validate_registration(
            provide_type, 
            register_type
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
        factory       : Callable[[Container], Any],
        resolve_type  : ResolveType
    ):
        self.__validate_registration(
            provide_type,
            register_type
        )
        
        self.registrations[provide_type] = _RegistrationPart(
            provide_type,
            register_type,
            factory,
            None,
            resolve_type
        )

        
        
    def resolve(self, data_type : _GenType) -> _GenType:
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
    
    

class _ConfigResolver:
    def __init__(
        self, 
        config_type    : Type,
        config_field   : str
    ):
        self.config_type    = config_type
        self.config_field   = config_field
        
    
    def __call__(self, container : Container) -> Type:
        if container.config is None:
            raise ValueError(f'Configuration in container is not loaded.')
            
        if not self.config_field in container.config:
            raise ValueError(f'{self.config_field} not present in configuration')

        config = deserialize_config(self.config_type, container.config[self.config_field], container.config_options)
        
        return config