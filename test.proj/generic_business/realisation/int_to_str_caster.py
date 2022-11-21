# project
from generic_business.interfaces import IProcessor

class IntToStrCaster(IProcessor[int, str]):
    def process(self, data: int) -> str:
        return f'({data})'