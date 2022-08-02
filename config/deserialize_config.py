# python
import numbers
from dataclasses import Field, fields
from typing import Type, List, Any
from typing import Dict
# 3rd party
from nameof import nameof
# project
from .deserialize_aux import is_list_alias, is_tuple_alias
from .deserialize_aux import get_list_alias_arg, get_tuple_alias_args
from .field_meta      import FieldMeta


def deserialize_item(item_type, item, meta_info):
    if item is None: return None
    
    deserialized_item = None
    
    if is_list_alias(item_type):
        deserialized_item = deserialize_list(item_type, item, meta_info)
    elif is_tuple_alias(item_type):
        deserialized_item = deserialize_tuple(item_type, item, meta_info)
    elif issubclass(item_type, str) and isinstance(item, str):
        deserialized_item = item_type(item)
    elif issubclass(item_type, numbers.Number) and isinstance(item, numbers.Number):
        deserialized_item = item_type(item)
    elif issubclass(item_type, bool) and isinstance(item, bool):
        deserialized_item = bool(item)
    else:
        deserialized_item = deserialize_config(item_type, item, meta_info)
    
    return deserialized_item
        

def deserialize_list(list_t, list, meta_info):
    item_type = get_list_alias_arg(list_t)
    
    deserialized_list = []
    for item in list:
        deserialized_list.append(deserialize_item(item_type, item, meta_info))
        
    return deserialized_list


def deserialize_tuple(tuple_type, list, meta_info):
    tuple_types = get_tuple_alias_args(tuple_type)
    
    if len(tuple_types) != len(list):
        raise ValueError('Len of types in tuple of class != len of list in config')
    
    deserialized_list = []
    for tuple_type, item in zip(tuple_types, list):
        deserialized_list.append(deserialize_item(tuple_type, item, meta_info))
        
    return tuple(deserialized_list)


def validate_fields_meta(meta_list):
    if not type(meta_list) is dict:
        raise ValueError(
            f'Type of field_meta in dataclass should be \'{nameof(dict)}\', '
            f'got type:{type(meta_list)}.'
        )
        
    for field_name, field_meta in meta_list.items():
        if not type(field_name) is str:
            raise ValueError(
                'Wrong type of key in fields_meta dict'
            )
        
        if not type(field_meta) is FieldMeta:
            raise ValueError(
                f'Wrong type of fields_meta dict element, '
                f'expected \'{nameof(FieldMeta)}\', gotted \'{type(field_meta)}\''
            )
        

def provide_fields_meta(
    type      : Type, 
    meta_info : dict
) -> Dict[str, FieldMeta]:
    real_meta = None
    
    if 'fields_meta' in type.__dict__:
        real_meta = type.__dict__['fields_meta']
    elif type in meta_info:
        real_meta = meta_info[type]
        
    if not real_meta is None:
        validate_fields_meta(real_meta)
        
    return real_meta


def deserialize_config(t, dict, meta_info = {}):
    t_params = {}
    
    # ToDo
    print(f'meta info:{meta_info}')
    print(f'type:{t}')
    
    fields_meta = provide_fields_meta(t, meta_info)
    
    # ToDo
    print(f'fields meta:{fields_meta}')
    print(f'')
    
    for field in fields(t):
        # default parsing
        parse_field_name = field.name
        specializer      = lambda dict_val : deserialize_item(field.type, dict_val, meta_info)
        
        # validation field meta
        if not fields_meta is None:
            if field.name in fields_meta:
                field_meta = fields_meta[field.name]
                parse_name = field_meta.parse_name
                if parse_name != '':
                    parse_field_name = parse_name

                # validation required
                if field_meta.required and not parse_field_name in dict:
                    raise ValueError(
                        f'Error during config parsing. Missing field \'{parse_field_name}\' in config '
                        f'that present field \'{field.name}\' in dataclass \'{t}\'.'
                    )
                    
                # if available specializer
                if not field_meta.specializer is None:
                    specializer = lambda dict_val : field_meta.specializer(dict_val)
                
        dict_value = dict[parse_field_name] if parse_field_name in dict else None
        
        deserialize_value = None
        if not dict_value is None:
            deserialize_value = specializer(dict_value)
    
        t_params[field.name] = deserialize_value
        
    return t(**t_params)