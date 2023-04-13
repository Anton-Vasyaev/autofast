import dependencies
# python
from dataclasses import dataclass
from typing      import List, Tuple
# project
from autofast.config import field_meta


ModelsListType = List[Tuple[str, int, bool]]

@dataclass
class EnvironmentSettings:
    checkpoint_path : str

    export_path : str
    
    models : ModelsListType

