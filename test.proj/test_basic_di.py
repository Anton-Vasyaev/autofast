import dependencies
# test
from autofast.injection import Container, ContainerOptions, ResolveType
from autofast.config    import ConfigurationOptions
# python
import json
# project
from business.interfaces    import *
from business.realisation   import *
from business.configuration import *


def test_basic_di():
    str_data = ['']
    
    options   = ContainerOptions(True)
    container = Container(options)
    
    with open('resources/business_config.json') as fh:
        config = json.load(fh)
        
    config_options = ConfigurationOptions(
        strong_enum_str=False,
        strong_number_matching=True
    )
    container.load_config(config, config_options)
    
    container.register_config(CityConfiguration, 'city')
    container.register_config(FormatConfiguration, 'format')
    container.register_config_by_name('mayor_config', MayorConfiguration, 'mayor')
    container.register_config(PrinterConfiguration, 'printer')
     
    
    container.register_factory(
        IPrinter,
        StrPrinter,
        lambda c : StrPrinter(c.resolve(PrinterConfiguration), str_data),
        ResolveType.Singleton
    )
    
    container.register_singleton(ICityProvider, ConfigCityProvider)

    container.register_factory_by_name(
        'mayor_provider',
        IMayorProvider,    
        ConfigMayorProvider,
        lambda c: ConfigMayorProvider(c.resolve_by_name('mayor_config', MayorConfiguration)),
        ResolveType.Singleton
    )
    container.register_factory(
        IMessageLoader, BarMessageLoader,
        lambda c : BarMessageLoader(c.resolve(ICityProvider), c.resolve_by_name('mayor_provider', IMayorProvider)),
        ResolveType.Singleton
    )
    container.register_singleton(IMessageFormatter, FooMessageFormatter)
    container.register_singleton(IDataProcessor,    StandardDataProcessor)
     
    processor = container.resolve(IDataProcessor)
    
    processor.process()
    
    assert str_data[0] == '[14:console]:ГОРОДОМ CHEREPOVETS С НАСЕЛЕНИЕМ 345612 ЧЕЛОВЕК УПРАВЛЯЕТ МЭР VASILIY PETROV [СКИЛЛ: 0.83, ВОЗРАСТ: 48].'