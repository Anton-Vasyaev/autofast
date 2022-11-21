# project
from generic_business.interfaces import IDataProvider


class StrProvider(IDataProvider[str]):
    data : str


    def __init__(self, data : str):
        self.data = data


    def provide_data(self) -> str:
        return self.data