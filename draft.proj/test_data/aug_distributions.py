# python
from dataclasses import dataclass
from typing import Tuple, List
# project
from fastdi.config import field_meta


@dataclass
class BasicColorDistribution:
    red   : Tuple[float, float]
    green : Tuple[float, float]
    blue  : Tuple[float, float]


@dataclass
class Rotate2Distribution:
    angles : Tuple[float, float]