# python
from copy import deepcopy
from typing import TypeVar, Generic, List
# project
from generic_business.interfaces import IDataProvider, ICollectionProvider

from .accumulate_processor import AccumulateProcessor


T = TypeVar('T')
V = TypeVar('V')

AccumulateT = TypeVar('AccumulateT')
ElementsT   = TypeVar('ElementsT')


class Accumulator(Generic[AccumulateT, ElementsT]):
    base : AccumulateT

    elements : List[ElementsT]

    accumulate_processor : AccumulateProcessor[AccumulateT, ElementsT]

    
    def __init__(
        self,
        base_provider        : IDataProvider[AccumulateT],
        elements_provider    : ICollectionProvider[ElementsT],
        accumulate_processor : AccumulateProcessor[AccumulateT, ElementsT]
    ):
        self.base = base_provider.provide_data()
        self.elements = elements_provider.provide_collection()
        self.accumulate_processor = accumulate_processor


    def process(self) -> AccumulateT:
        base = deepcopy(self.base)

        for i in range(len(self.elements) - 1):
            first  = self.elements[i]
            second = self.elements[i + 1]

            base += self.accumulate_processor.process(first, second) # type: ignore

        return base

            