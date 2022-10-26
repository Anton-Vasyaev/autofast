import dependencies
# project
from ..interfaces    import IMayorProvider
from ..data          import MayorData
from ..configuration import MayorConfiguration



class ConfigMayorProvider(IMayorProvider):
    def __init__(self, config : MayorConfiguration):
        self.config = config
    
    def provide_mayor(self) -> MayorData:
        return MayorData(
            self.config.name,
            self.config.age,
            self.config.skills
        )