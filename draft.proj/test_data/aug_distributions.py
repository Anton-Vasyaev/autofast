# python
from dataclasses import dataclass
from typing import Optional, Tuple, List
# project
from autofast.config import field_meta


@dataclass
class BasicColorDistribution:
    red   : Tuple[float, float]
    green : Tuple[float, float]
    blue  : Tuple[float, float]


@dataclass
class ColorNoiseDistribution:
    red   : Tuple[float, float]
    green : Tuple[float, float]
    blue  : Tuple[float, float]


@dataclass
class IntensityNoiseDistribution:
    intensity : Tuple[float, float]


@dataclass
class Rotate3Distribution:
    angles : Tuple[float, float, float]


@dataclass
class MirrorDistribution:
    horizontal : float
    vertical   : float


@dataclass
class AugmentationDistribution:
    basic_color     : Optional[BasicColorDistribution]
    color_noise     : Optional[ColorNoiseDistribution]
    intensity_noise : Optional[IntensityNoiseDistribution]

    rotate_3d : Optional[Rotate3Distribution]
    mirror    : Optional[MirrorDistribution]