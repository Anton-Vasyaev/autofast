# python
from dataclasses import dataclass
from typing import List, Tuple
from enum   import IntEnum
# 3rd party
from nameof import nameof


class Color(IntEnum):
    RED   = 0
    GREEN = 1
    BLUE  = 2
    
    def __init__(self, value):
        if not isinstance(value, str):
            raise Exception(f'invalid init type \'{type(value)}\' for enum \'{nameof(Color)}\'')
    
    
    
    

def typing_example():
    p = Point(5, 3)
    
    print(p.точка_х)
    print(p.точка_у)
    
    
if __name__ == '__main__':
    typing_example()