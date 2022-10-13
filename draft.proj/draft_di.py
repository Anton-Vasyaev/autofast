import dependencies
# python
from abc import ABC, abstractmethod
# project
from fastdi.injection import Container, ResolveType


class IntDataConfig:
    def __init__(self, data : int):
        self.data = data
        
        
    def get_int_data(self):
        return self.data
    


class IDataProvider(ABC):
    @abstractmethod
    def provide_data(self) -> str:
        raise NotImplementedError()
    
    
    
class StrDataProvider(IDataProvider):
    def __init__(self, message : str):
        self.message = message
    
    def provide_data(self) -> str:
        return self.message
    
    
    
class IDataReceiver(ABC):
    @abstractmethod
    def receive_data(self, data : str) -> None:
        raise NotImplementedError()
    
    
    
class ConsoleDataReceiver(IDataReceiver):
    def __init__(self, id : int):
        self.id = id
        
        
    def receive_data(self, data : str) -> None:
        print(f'[{self.id}]: data receive:{data}')
        
        
        
class IPipeProcessor(ABC):
    @abstractmethod
    def process_data(self) -> None:
        raise NotImplementedError()
    

class FooPipeProcessor(IPipeProcessor):
    def __init__(
        self,
        data_provider : IDataProvider,
        data_receiver : IDataReceiver
    ):
        self.data_provider = data_provider
        self.data_receiver = data_receiver
        
        
    def process_data(self) -> None:
        data = self.data_provider.provide_data()
        
        self.data_receiver.receive_data(data)
        
        
        
def draft_di():
    container = Container() 
    
    container.register_factory(
        IntDataConfig,
        IntDataConfig,
        lambda c : IntDataConfig(16),
        ResolveType.Singleton
    )
    
    container.register_factory(
        IDataProvider, 
        StrDataProvider, 
        lambda c : StrDataProvider('jonny_gutling'),
        ResolveType.Singleton
    )
    container.register_type(IDataReceiver, ConsoleDataReceiver, ResolveType.Singleton)
    
    container.register_type(IPipeProcessor, FooPipeProcessor, ResolveType.Singleton)

    pipe : FooPipeProcessor = container.resolve(IPipeProcessor)
    
    pipe.process_data()




if __name__ == '__main__':
    draft_di()