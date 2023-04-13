# python
from dataclasses import dataclass
# project
from autofast.config import field_meta



@dataclass
class PrinterConfiguration:
    name : str

    id : int 