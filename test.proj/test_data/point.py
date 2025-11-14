# python
from dataclasses import dataclass
from typing      import List, cast
# 3rd party
from varname import nameof
# project
from autofast.config.parse_graph import Node, ListNode


@dataclass
class Point2:
    x : float
    y : float


def point_decoder(node : Node) -> Point2:
    if not isinstance(node, ListNode):
        raise Exception(
            f'Cannot convert dict node to {nameof(Point2)}. Node is not List'
        )
    
    list_node = cast(Node, node)

    list_data = list_node.list_data

    validate_exception = Exception(f'{nameof(Point2)} list not has two number values')
    if len(list_data) != 2:
        raise validate_exception
    

    p = Point2(float(list_data[0].value), float(list_data[1].value))

    return p


def point_encoder(point : Point2) -> List[float]:
    return [point.x, point.y]
