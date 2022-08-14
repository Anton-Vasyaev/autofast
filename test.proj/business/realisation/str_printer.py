# python
from typing import Any
# project
from ..interfaces    import IPrinter
from ..configuration import PrinterConfiguration


class StrPrinter(IPrinter):
    def __init__(
        self,
        config   : PrinterConfiguration,
        str_data : list
    ):
        self.config   = config
        self.str_data = str_data
    
    
    def print_data(self, data: Any):
        self.str_data[0] = f'[{self.config.id}:{self.config.name}]:{data}'