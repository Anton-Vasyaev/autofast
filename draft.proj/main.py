import dependencies
# python
from dataclasses import dataclass, field
from enum        import IntEnum
from typing      import List, Tuple
# 3rd party
from easydict import EasyDict
from nameof   import nameof
#project
from fastdi.config import deserialize_config
from fastdi.config import FieldMeta, field_meta


class DivisionType(IntEnum):
    INFANTRY = 0
    TANK     = 1


class GeneralRang(IntEnum):
    MAJOR        = 0
    COLONEL      = 1
    LEUTENANT    = 2
    MARSHAL      = 3
    FIELDMARSHAL = 4
    

@dataclass
class Division:
    FIELDS_META = {
        'division_type' : FieldMeta(required=True, parse_name='div_type'),
        'city'          : FieldMeta(required=True, parse_name='GOROD')
    }

    name            : str
    division_type   : DivisionType = field_meta(required=True, parse_name='DIVT')
    reserve         : bool  = field_meta(required=True, default=False)
    soldiers        : int   = field_meta(default=0)
    tanks           : int   = field_meta(default=0)
    city            : str   = field_meta(required=True, parse_name='GOROD', default='')
    morale          : float = 0.0
    metrics         : dict  = field_meta(default_factory = dict)
    hq              : List[Tuple[str, GeneralRang, float]] = field_meta(required=True, default_factory= list)
    

@dataclass
class Army:
    FIELDS_META = {
        'general' : FieldMeta(required=True)
    }
    
    name            : str
    general         : str 
    divisions       : List[Division]
    organisation    : float
    base            : str


    
    
def inspect_example():
    division_meta = {
        'division_type' : FieldMeta(required=True, parse_name='d_type'),
        'soldiers'      : FieldMeta(required=True, parse_name='SOLS'),
        'type'          : FieldMeta(required=True),
    }
    
    army_meta_info = {
        Division : division_meta
    }
    
    takistan_army_config = {
        'name' : '2nd east Army',
        
        'general' : 'Rudolf',
        
        'divisions' : [
            {
                'name' : '1st grenadier',
                'd_type' : 'infantry',
                'reserve' : False,
                'SOLS' : 8943,
                'tanks' : 25,
                'GOROD' : 'ust-lupinsk',
                'morale' : 93.0,
                'hq' : [
                    ['Andrew Menderlson',    'colonel',   0.5],
                    ['Vasiliy Pirogov',      'leutenant', 0.3],
                    ['Archibald Shipuchkin', 'major',     0.7]
                ]
            },
            {
                'name'  : '2nd tank',
                'd_type'  : 1,
                'reserve' : True,
                'SOLS'  : 5644,
                'tanks' : 166,
                'GOROD' : 'new-deli',
                'hq' : [
                    ['Konstantin Pilulkin', 'fieldmarshal', 0.63],
                    ['Sergey Vasilkov',     'marshal',      0.13]
                ]
            }
        ],
        
        'organisation' : 85.23,
        
        'base' : 'Zagrabad',
    }
    
    takistan_army_ed = EasyDict(takistan_army_config)
    
    takistan_army = deserialize_config(Army, takistan_army_ed, army_meta_info)

    print(takistan_army)
    

    

if __name__ == '__main__':
    inspect_example()