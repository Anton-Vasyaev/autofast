import dependencies
# python
from dataclasses import dataclass
from typing      import List, Tuple
# project
from autofast.config import field_meta


ModelsListType = List[Tuple[str, int, float]]

@dataclass
class EnvironmentSettings:
    checkpoint_path : str            = field_meta(required=True)
    export_path     : str            = field_meta(required=True)
    models          : ModelsListType = field_meta(required=True)

