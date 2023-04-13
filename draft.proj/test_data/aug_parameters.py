from dataclasses import dataclass
from .aug_distributions import *

@dataclass
class AugmentationParameters:
    aug_dist    : AugmentationDistribution
    aug_size    : float
    random_seed : int = field_meta(default=1024)