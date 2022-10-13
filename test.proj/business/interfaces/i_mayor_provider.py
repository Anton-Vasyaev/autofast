# python
from abc import ABC, abstractmethod
# project
from ..data import MayorData


class IMayorProvider:
    @abstractmethod
    def provide_major(self) -> MayorData:
        raise NotImplementedError()