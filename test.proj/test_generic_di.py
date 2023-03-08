import dependencies
# test
from autofast.injection import Container, ContainerOptions, ResolveType
from autofast.config    import ConfigurationOptions
# python
import json
# project
from generic_business.interfaces import *
from generic_business.logic      import *
from generic_business.realisation import *


def test_basic_di():
    options = ContainerOptions(True)
    
    options   = ContainerOptions(True)
    container = Container(options)

    container.register_factory(
        IDataProvider[str], 
        StrProvider, 
        lambda c : StrProvider('result:'),
        ResolveType.Singleton
    )

    container.register_factory(
        ICollectionProvider[int],
        IntListProvider,
        lambda c : IntListProvider([1, 2, 3, 4, 5, 6, 7]),
        ResolveType.Singleton
    )

    container.register_singleton(IBinaryOperation[int], Summator[int])
    container.register_singleton(IUnaryOperation[str], SquareBracketDecorator)
    container.register_singleton(IProcessor[int, str], IntToStrCaster)

    container.register_singleton(AccumulateProcessor[str, int], AccumulateProcessor[str, int])
    container.register_singleton(Accumulator[str, int], Accumulator[str, int])

    accumulator = container.resolve(Accumulator[str, int])

    assert accumulator.process() == 'result:[(3)][(5)][(7)][(9)][(11)][(13)]'