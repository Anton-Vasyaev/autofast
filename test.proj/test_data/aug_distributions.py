# python
from dataclasses import dataclass
from typing import Tuple, List
from enum import Enum, auto
# project
from autofast.config import field_meta


@dataclass
class BasicColorDistribution:
    red   : Tuple[float, float] = field_meta(required=True)
    green : Tuple[float, float] = field_meta(required=True)
    blue  : Tuple[float, float] = field_meta(required=True)


@dataclass
class Rotate3Distribution:
    angles : Tuple[float, float, float] = field_meta(required=True)


@dataclass
class MirrorDistribution:
    horizontal : float = field_meta(required=True)
    vertical   : float = field_meta(required=True)


class StretchOrientationType(Enum):
    HORIZONTAL = auto()
    VERTICAL   = auto()
    

class StretchImageType(Enum):
    SRC = auto()
    DST = auto()
    
    
@dataclass
class StretchDistribution:
    orientation : StretchOrientationType
    image       : StretchImageType



@dataclass
class AugmentationDistribution:
    basic_color     : BasicColorDistribution

    rotate_3d : Rotate3Distribution
    mirror    : MirrorDistribution
    
    stretch : StretchDistribution