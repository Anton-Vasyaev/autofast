# python
from abc import abstractmethod



class IDataProcessor:
    @abstractmethod
    def process(self):
        raise NotImplementedError()