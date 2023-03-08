# python
from dataclasses import dataclass
from typing import Tuple, List
# project
from autofast.config import field_meta


@dataclass
class BasicColorDistribution:
    red   : Tuple[float, float] = field_meta(required=True)
    green : Tuple[float, float] = field_meta(required=True)
    blue  : Tuple[float, float] = field_meta(required=True)


@dataclass
class ColorNoiseDistribution:
    red   : Tuple[float, float] = field_meta(required=True)
    green : Tuple[float, float] = field_meta(required=True)
    blue  : Tuple[float, float] = field_meta(required=True)


@dataclass
class IntensityNoiseDistribution:
    intensity : Tuple[float, float] = field_meta(required=True)


@dataclass
class Rotate3Distribution:
    angles : Tuple[float, float, float] = field_meta(required=True)


@dataclass
class MirrorDistribution:
    horizontal : float = field_meta(required=True)
    vertical   : float = field_meta(required=True)


@dataclass
class AugmentationDistribution:
    basic_color     : BasicColorDistribution
    color_noise     : ColorNoiseDistribution
    intensity_noise : IntensityNoiseDistribution

    rotate_3d : Rotate3Distribution
    mirror    : MirrorDistribution