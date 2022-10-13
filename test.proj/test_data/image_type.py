from enum import Enum, auto


class ImageType(Enum):
    RGB  = auto()
    RGBA = auto()
    BGR  = auto()
    BGRA = auto()
    GRAY = auto()
    HSV  = auto()