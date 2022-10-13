# python
from dataclasses import dataclass
from enum import Enum, auto
# project
from fastdi.config import field_meta


class LanguageType(Enum):
    ENGLISH = auto()
    RUSSIAN = auto()
    
    
class WordType(Enum):
    LOWER = auto()
    UPPER = auto()
    

@dataclass
class FormatConfiguration:
    language_type : LanguageType = field_meta(required=True)
    word_type     : WordType     = field_meta(required=True)