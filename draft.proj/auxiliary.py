import dependencies
# python
from typing import cast
# project
from autofast.reflection.data import ClassMetaInfo

def print_class_meta_info(
    info : ClassMetaInfo,
    tab  : int = 0
):
    tab_str = '\t' * tab
    print(f'{tab_str}type:{info.type}')
    for func in info.functions:
        print(f'{tab_str} |-\'{func}\'')

    if len(info.parents) == None:
        return
        
    for parent in info.parents:
        parent_info = cast(ClassMetaInfo, parent)
        print_class_meta_info(parent_info, tab + 1)
