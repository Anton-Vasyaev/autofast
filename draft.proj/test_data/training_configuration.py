# python
from dataclasses import dataclass, field
from typing      import Optional
# project
from autofast.config import field_meta

from .training_parameters import TrainingParameters
from .environment_settings import EnvironmentSettings
from .aug_parameters       import AugmentationParameters

@dataclass
class TrainingConfiguration:
    train_params : TrainingParameters
    env_settings : EnvironmentSettings
    aug_params   : Optional[AugmentationParameters]