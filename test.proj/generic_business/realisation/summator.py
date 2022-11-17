# python
from typing import TypeVar, Generic
# project
from generic_business.interfaces import IBinaryOperation
from generic_business.auxiliary  import SupportsAdd

T = TypeVar('T')


class Summator(IBinaryOperation[T]):
    def operate(self, left_op: T, right_op: T) -> T:
        return left_op + right_op # type: ignore