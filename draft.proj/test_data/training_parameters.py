from urllib import request
import dependencies
# python
from dataclasses import dataclass
from typing      import Tuple, List
# project
from autofast.config import field_meta

from .image_type import ImageType


@dataclass
class TrainingParameters:
    input_size    : Tuple[int, int]
    image_type    : ImageType
    batch_size    : int
    epochs        : int
    learning_rate : float           = field_meta(default=1e-3)
    use_gpu       : bool            = field_meta(default=True)

