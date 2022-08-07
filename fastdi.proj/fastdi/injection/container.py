# python
from typing import Any, Callable, List, Type
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
    

class ResolveType:
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
            None,
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

        
        
    def resolve_type(self, data_type : Type):
        pass
        
    

        
@dataclass
class _RegistrationPart:
    provide_type  : Type
    register_type : Type
    factory       : Callable[[Container], Any]
    instance      : Any
    resolve_type  : ResolveType
