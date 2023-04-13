# python
from dataclasses import dataclass, field
from typing      import Dict, Type, Optional
# project
from .field_meta_data import FieldMeta, DecoderType, EncoderType


FieldMetaInfoType = Dict[Type, Dict[str, FieldMeta]]



@dataclass
class TypeConfigInfo:
    encoder : Optional[EncoderType] = None
    decoder : Optional[DecoderType] = None


TypesConfigInfoType = Dict[Type, TypeConfigInfo]


@dataclass
class ConfigurationOptions:
    field_info : FieldMetaInfoType = field(default_factory=dict)

    types_info : TypesConfigInfoType = field(default_factory=dict)

    strong_enum_str : bool = False

    strong_number_matching : bool = False 