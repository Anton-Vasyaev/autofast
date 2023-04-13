# python
from dataclasses import dataclass
from typing import Tuple, Optional
from enum import Enum, auto
# project
from autofast.config import field_meta


@dataclass
class BasicColorDistribution:
    red : Tuple[float, float]

    green : Tuple[float, float]

    blue : Tuple[float, float]


@dataclass
class Rotate3Distribution:
    angles : Tuple[float, float, float]


@dataclass
class MirrorDistribution:
    horizontal : float

    vertical : float


class StretchOrientationType(Enum):
    HORIZONTAL = auto()
    VERTICAL   = auto()
    

class StretchImageType(Enum):
    SRC = auto()
    DST = auto()
    
    
@dataclass
class StretchDistribution:
    orientation : StretchOrientationType

    image : StretchImageType


@dataclass
class NoiseDeltaDistribution:
    low : float

    upper : float


@dataclass
class AugmentationDistribution:
    basic_color : Optional[BasicColorDistribution]

    rotate_3d : Optional[Rotate3Distribution]

    mirror : Optional[MirrorDistribution]
    
    stretch : Optional[StretchDistribution]

    noise_delta : Optional[NoiseDeltaDistribution]