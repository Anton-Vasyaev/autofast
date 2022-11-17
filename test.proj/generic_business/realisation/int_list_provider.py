# python
from typing import List
# project
from generic_business.interfaces import ICollectionProvider


class IntListProvider(ICollectionProvider[int]):
    data : List[int]


    def __init__(self, data : List[int]):
        self.data = data


    def provide_collection(self) -> List[int]:
        return self.data