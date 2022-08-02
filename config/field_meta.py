from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class FieldMeta:
    required    : bool = False
    parse_name  : str = ''
    specializer : Callable[[Any], Any] = None