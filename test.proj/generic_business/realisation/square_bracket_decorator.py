# project
from generic_business.interfaces import IUnaryOperation


class SquareBracketDecorator(IUnaryOperation[str]):
    def operate(self, data: str) -> str:
        return f'[{data}]'