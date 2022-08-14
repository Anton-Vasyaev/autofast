# project
from ..interfaces import IMayorProvider
from ..data import MayorData



class RussianMayorProvider(IMayorProvider):
    def provide_major(self) -> MayorData:
        return MayorData("Vasiliy Ivanov", 48, 0.74)