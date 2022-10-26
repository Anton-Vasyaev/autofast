# python
from abc import ABC, abstractmethod
# project
from ..data import MayorData


class IMayorProvider(ABC):
    @abstractmethod
    def provide_mayor(self) -> MayorData:
        raise NotImplementedError()