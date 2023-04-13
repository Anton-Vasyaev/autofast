# python
from abc import abstractmethod
# project
from ..data import MayorData


class IMayorProvider:
    @abstractmethod
    def provide_mayor(self) -> MayorData:
        raise NotImplementedError()