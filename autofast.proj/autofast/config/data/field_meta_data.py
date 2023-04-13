from dataclasses import dataclass, MISSING
from dataclasses import field, Field
from typing import Any, Callable, Optional, Dict
from ..parse_graph import Node


FIELDMETA_KEYNAME = 'autofast_meta'


DecoderType = Optional[Callable[[Node], Any]]
EncoderType = Optional[Callable[[Any], Any]]



@dataclass
class FieldMeta:
    parse_name : str  = ''
    decoder    : DecoderType = None
    encoder    : EncoderType = None


    @staticmethod
    def to_dict(
        parse_name : str         = '',
        decoder    : DecoderType = None,
        encoder    : EncoderType = None
    ):
        return {
            FIELDMETA_KEYNAME : FieldMeta(parse_name, decoder, encoder)
        }


def field_meta(
    parse_name : str                  = '',
    decoder    : DecoderType          = None,
    encoder    : EncoderType          = None,
    default                           = MISSING, 
    default_factory                   = MISSING, 
    init                              = True, 
    repr                              = True,
    hash                              = None, 
    compare                           = True, 
    metadata                          = None
):
    meta_dict = FieldMeta.to_dict(parse_name, decoder, encoder)

    if not metadata is None:
        meta_dict.update(metadata)

    return field(
        default         = default, 
        default_factory = default_factory,
        init            = init,
        repr            = repr,
        hash            = hash,
        compare         = compare,
        metadata        = meta_dict
    )