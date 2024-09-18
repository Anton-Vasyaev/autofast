# python
from dataclasses import dataclass, field
from typing      import Optional, Dict, Tuple
# project
from autofast.config import field_meta

from .training_parameters  import TrainingParameters
from .environment_settings import EnvironmentSettings
from .aug_parameters       import AugmentationParameters

@dataclass
class DeviceInfo:
    device_name : str

    device_id : int

    vendor : str

PerformanceCapacityType = Tuple[float, float]

HardwareSettings = Tuple[PerformanceCapacityType, str, str]


@dataclass
class TrainingConfiguration:
    train_params : TrainingParameters

    env_settings : EnvironmentSettings
    
    aug_params   : Optional[AugmentationParameters]
    
    module_name : Optional[str]

    hardware_settings : HardwareSettings

    custom_devices : Dict[str, DeviceInfo] = field_meta(default_factory=dict)