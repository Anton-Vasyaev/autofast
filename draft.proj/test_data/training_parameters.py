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
    input_size    : Tuple[int, int] = field_meta(required=True)
    image_type    : ImageType       = field_meta(required=True)
    batch_size    : int             = field_meta(required=True)
    epochs        : int             = field_meta(required=True)
    learning_rate : float           = field_meta(required=True, default=1e-3)
    use_gpu       : bool            = field_meta(required=True, default=True)

