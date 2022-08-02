# python
from dataclasses import dataclass, field
from enum        import IntEnum
from typing      import List
# 3rd party
from easydict import EasyDict
from nameof   import nameof
#project
from config import deserialize_config
from config import FieldMeta


class DivisionType(IntEnum):
    INFANTRY = 0
    TANK     = 1
    

@dataclass
class Division:
    name     : str
    type     : DivisionType
    soldiers : int
    tanks    : int
    city     : str   = field
    morale   : float = 0.0
    metrics  : dict  = field(default_factory=dict)
    

@dataclass
class Army:
    fields_meta = {
        'general' : FieldMeta(required=True)
    }
    
    name            : str
    general         : str 
    divisions       : List[Division]
    organisation    : float
    base            : str


    
    
def inspect_example():
    division_meta = {
        'soldiers' : FieldMeta(required=True, parse_name='SOLS'),
        'type'     : FieldMeta(required=True),
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
                'type' : 'INFANTRY',
                'SOLS' : 8943,
                'tanks' : 25,
                'morale' : 93.0
            },
            {
                'name'  : '2nd tank',
                'type'  : 1,
                'SOLS'  : 5644,
                'tanks' : 166
            }
        ],
        
        'organisation' : 85.23,
        
        'base' : 'Zagrabad',
    }
    
    takistan_army_ed = EasyDict(takistan_army_config)
    
    takistan_army = deserialize_config(Army, takistan_army_ed)

    print(takistan_army)
    

    

if __name__ == '__main__':
    inspect_example()