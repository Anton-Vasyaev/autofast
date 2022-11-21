from typing import TypeVar, Generic
# project
from generic_business.interfaces import IProcessor, IBinaryOperation, IUnaryOperation

AccumulateT = TypeVar('AccumulateT')
ElementsT   = TypeVar('ElementsT')


class AccumulateProcessor(Generic[AccumulateT, ElementsT]):
    operation : IBinaryOperation[ElementsT]
    caster    : IProcessor[ElementsT, AccumulateT]
    decorator : IUnaryOperation[AccumulateT]

    def __init__(
        self,
        operation : IBinaryOperation[ElementsT],
        caster    : IProcessor[ElementsT, AccumulateT],
        decorator : IUnaryOperation[AccumulateT]
    ):
        self.operation = operation
        self.caster    = caster
        self.decorator = decorator


    def process(self, left_op : ElementsT, right_op : ElementsT) -> AccumulateT:
        result_op   = self.operation(left_op, right_op)
        cast_op     = self.caster(result_op)
        decorate_op = self.decorator(cast_op)

        return decorate_op