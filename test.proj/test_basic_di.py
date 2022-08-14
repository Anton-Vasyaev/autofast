import dependencies
# test
from fastdi.injection import Container, ContainerOptions, ResolveType
# project
from business.interfaces import *
from business.realisation import *


def test_basic_di():
    str_data = ['']
    
    options   = ContainerOptions(True)
    container = Container(options)
    
    container.register_factory(
        IPrinter,
        StrPrinter,
        lambda c : StrPrinter(str_data),
        ResolveType.Singleton
    )
    
    container.register_type(ICityProvider,     RussianCityProvider,   ResolveType.Singleton)
    container.register_type(IMayorProvider,    RussianMayorProvider,  ResolveType.Singleton)
    container.register_type(IMessageLoader,    BarMessageLoader,      ResolveType.Singleton)
    container.register_type(IMessageFormatter, FooMessageFormetter,   ResolveType.Singleton)
    container.register_type(IDataProcessor,    StandardDataProcessor, ResolveType.Singleton)
    
    
    processor = container.resolve(IDataProcessor)
    
    processor.process()
    
    assert str_data[0] == 'Городом cherepovets с населением 340521 человек управляет мэр Vasiliy Ivanov [Скилл: 0.74, возраст: 48].'