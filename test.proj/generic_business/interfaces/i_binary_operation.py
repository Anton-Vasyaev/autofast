# python
from abc    import abstractmethod
from typing import TypeVar, Generic


T = TypeVar('T')


class IBinaryOperation(Generic[T]):
    @abstractmethod
    def operate(self, left_op : T, right_op : T) -> T:
        raise NotImplementedError()


    def __call__(self, left_op : T, right_op : T) -> T:
        return self.operate(left_op, right_op)