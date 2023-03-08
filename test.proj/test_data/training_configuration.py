# python
from dataclasses import dataclass, field
# project
from autofast.config import field_meta

from .training_parameters import TrainingParameters
from .environment_settings import EnvironmentSettings
from .aug_parameters       import AugmentationParameters

@dataclass
class TrainingConfiguration:
    train_params : TrainingParameters     = field_meta(required=True)
    env_settings : EnvironmentSettings    = field_meta(required=True)
    aug_params   : AugmentationParameters = field_meta()
    
    module_name : str = field_meta()