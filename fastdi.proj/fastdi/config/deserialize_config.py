# python
import numbers
from dataclasses import MISSING, dataclass, fields, field
from types import MappingProxyType
from typing import Type, List, Any, TypeVar
from typing import Dict
from enum import Enum, IntEnum
# 3rd party
from nameof import nameof
# project
from .deserialize_aux import is_list_alias, is_tuple_alias
from .deserialize_aux import get_list_alias_arg, get_tuple_alias_args
from .field_meta_data import FieldMeta, FIELDMETA_KEYNAME


__GenType = TypeVar('__GenType')

MetaInfoType = Dict[Type, Dict[str, FieldMeta]]

@dataclass
class _DeserializeOptions:
    meta_info       : MetaInfoType = field(default_factory=dict)
    strong_enum_str : bool         = False



def _deserialize_item(
    item_type : Type, 
    item      : Any, 
    options   : _DeserializeOptions
):
    if item is None: return None
    
    deserialized_item = None
    
    # deserialize list part
    if is_list_alias(item_type):
        deserialized_item = _deserialize_list(item_type, item, options)

    # deserialize list part that a present tuple
    elif is_tuple_alias(item_type):
        deserialized_item = _deserialize_tuple(item_type, item, options)
    
    # deserialize str
    elif issubclass(item_type, str) and isinstance(item, str):
        deserialized_item = item_type(item)

    # deserialize IntEnum
    elif issubclass(item_type, IntEnum) and isinstance(item, int):
        deserialized_item = item_type(item)

    # deserialize Enum
    elif issubclass(item_type, Enum) and isinstance(item, str):
        #raise NotImplementedError(f'Not implemented deserialize {nameof(Enum)}.')
        deserialized_item = _deserialize_enum_str(item_type, item, options)

    # deserialize number
    elif issubclass(item_type, numbers.Number) and isinstance(item, numbers.Number):
        deserialized_item = item_type(item)

    # deserialize bool
    elif issubclass(item_type, bool) and isinstance(item, bool):
        deserialized_item = bool(item)

    # deserialize dict
    else:
        deserialized_item = _deserialize_config(item_type, item, options)
    
    return deserialized_item
        

def _deserialize_list(
    list_t  : Any, 
    list    : list, 
    options : _DeserializeOptions
):
    item_type = get_list_alias_arg(list_t)
    
    deserialized_list = []
    for item in list:
        deserialized_list.append(_deserialize_item(item_type, item, options))
        
    return deserialized_list


def _deserialize_tuple(
    tuple_type  : Any, 
    list        : list, 
    options     : _DeserializeOptions
):
    tuple_types = get_tuple_alias_args(tuple_type)
    
    if len(tuple_types) != len(list):
        raise ValueError('Len of types in tuple of class != len of list in config')
    
    deserialized_list = []
    for tuple_type, item in zip(tuple_types, list):
        deserialized_list.append(_deserialize_item(tuple_type, item, options))
        
    return tuple(deserialized_list)


def _deserialize_enum_str(
    enum_type : Type,
    item      : str,
    options   : _DeserializeOptions
):
    elements_data = { }
    for el in enum_type:
        if not options.strong_enum_str:
            elements_data[el.name.lower()] = el
        else:
            elements_data[el.name] = el

    key_item = item.lower() if not options.strong_enum_str else item

    return elements_data[key_item]


def _validate_fields_meta(
    meta_list : Any
):
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
                f'Wrong type of fields_meta in field \'{field_name}\', '
                f'expected \'{nameof(FieldMeta)}\', gotted \'{type(field_meta)}\''
            )
        

def _provide_fields_meta(
    data_type : Type, 
    meta_info : MetaInfoType
) -> Dict[str, FieldMeta]:
    type_meta = {}

    # write local fields params
    for field in fields(data_type):
        if isinstance(field.metadata, MappingProxyType):
            if FIELDMETA_KEYNAME in field.metadata:
                type_meta[field.name] = field.metadata['fastdi_meta']

    # rewrite meta from static field FIELDS_META
    if hasattr(data_type, "FIELDS_META"):
        type_fields_meta = data_type.FIELDS_META

        for field_name, field_meta in type_fields_meta.items():
            type_meta[field_name] = field_meta

    # rewrite global params
    if data_type in meta_info:
        type_fields_meta = meta_info[data_type]

        for field_name, field_meta in type_fields_meta.items():
            type_meta[field_name] = field_meta


    _validate_fields_meta(type_meta)
        
    return type_meta


def _deserialize_config(
    data_type : __GenType, 
    dict_data : dict,
    options   : _DeserializeOptions
) -> __GenType:
    t_params = {}
    
    fields_meta = _provide_fields_meta(data_type, options.meta_info)
    
    for field in fields(data_type):
        # default parsing
        parse_field_name = field.name
        decoder      = lambda dict_val : _deserialize_item(field.type, dict_val, options)
        
        # validation field meta
        if not fields_meta is None:
            if field.name in fields_meta:
                field_meta = fields_meta[field.name]
                parse_name = field_meta.parse_name
                if parse_name != '':
                    parse_field_name = parse_name

                # validation required
                if field_meta.required and not parse_field_name in dict_data:
                    raise ValueError(
                        f'Error during config parsing. Missing field \'{parse_field_name}\' in config '
                        f'that present field \'{field.name}\' in dataclass \'{data_type}\'.'
                    )
                    
                # if available decoder
                if not field_meta.decoder is None:
                    decoder = lambda dict_val : field_meta.decoder(dict_val)

        dict_value = dict_data[parse_field_name] if parse_field_name in dict_data else None
        
        deserialize_value = None
        if not dict_value is None:
            deserialize_value = decoder(dict_value)

        # set default value if field not available in configuration
        if deserialize_value is None:
            if not field.default is MISSING:
                deserialize_value = field.default
            elif not field.default_factory is MISSING:
                deserialize_value = field.default_factory()

    
        t_params[field.name] = deserialize_value
        
    return data_type(**t_params)


def deserialize_config(
    data_type       : __GenType,
    dict_data       : dict,
    meta_info       : MetaInfoType = {},
    strong_enum_str : bool         = False
) -> __GenType:
    options = _DeserializeOptions(
        meta_info, 
        strong_enum_str
    )

    return _deserialize_config(data_type, dict_data, options)