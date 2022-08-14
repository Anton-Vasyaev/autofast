# python
from typing import Any
# project
from ..interfaces import IPrinter



class StrPrinter(IPrinter):
    def __init__(self, str_data : list):
        self.str_data = str_data
    
    
    def print_data(self, data: Any):
        self.str_data[0] = f'{data}'