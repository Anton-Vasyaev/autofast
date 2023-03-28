import dependencies
# python
from typing import List 
from dataclasses import dataclass, fields
# project
from autofast.config import field_meta, serialize_config


@dataclass
class Point:
    x : float = field_meta(required=True)
    
    y : float = field_meta(required=True)


@dataclass
class Zone:
    name : str = field_meta(required=True, parse_name='zone_id')

    polygon : List[Point] = field_meta(required=True)

    enable_cache : bool = field_meta(required=True)

    detections_count : int = field_meta(required=True)


if __name__ == '__main__':
    a = Zone(
        'adolf',
        [Point(1, 2), Point(2, 3), Point(4, 5)],
        True,
        5
    )

    a = serialize_config(a)
    
    print(a)