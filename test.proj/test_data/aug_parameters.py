from dataclasses import dataclass
from typing      import Optional
# project
from .aug_distributions import *

@dataclass
class AugmentationParameters:
    aug_dist : Optional[AugmentationDistribution]

    aug_size : float
    
    random_seed : int