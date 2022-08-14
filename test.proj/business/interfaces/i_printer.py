# python
from abc import ABC, abstractmethod
from typing import Any


class IPrinter(ABC):
    def print_data(self, data : Any):
        raise NotImplementedError()