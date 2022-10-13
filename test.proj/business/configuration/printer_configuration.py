# python
from dataclasses import dataclass
# project
from fastdi.config import field_meta



@dataclass
class PrinterConfiguration:
    name : str = field_meta(required=True)
    id   : int = field_meta(required=True)