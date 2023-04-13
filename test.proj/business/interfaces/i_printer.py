# python
from abc import abstractmethod
from typing import Any


class IPrinter:
    @abstractmethod
    def print_data(self, data : Any):
        raise NotImplementedError()