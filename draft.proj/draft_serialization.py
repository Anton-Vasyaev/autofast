import dependencies
# python
from typing import List 
from dataclasses import dataclass, fields
# project
from autofast.config import field_meta, serialize_config


@dataclass
class Point:
    x : float
    
    y : float


@dataclass
class Zone:
    name : str = field_meta(parse_name='zone_id')

    polygon : List[Point]

    enable_cache : bool

    detections_count : int


if __name__ == '__main__':
    a = Zone(
        'adolf',
        [Point(1, 2), Point(2, 3), Point(4, 5)],
        True,
        5
    )

    a = serialize_config(a)
    
    print(a)