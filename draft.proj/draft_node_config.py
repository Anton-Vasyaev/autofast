import dependencies
# python
import json
# project
from fastdi.config.parse_graph.node import Node, DictNode, ListNode, ValueNode


def get_full_path(node : Node):
    if node.parent is None:
        return []
    
    data_list = get_full_path(node.parent) + [node.key_name]
    
    return data_list


def recursive_enumerate(node : Node):
    if isinstance(node, DictNode):
        node : DictNode = node
        for key, item in node.dict_data.items():
            recursive_enumerate(item)
    elif isinstance(node, ListNode):
        node : ListNode = node
        for item in node.list_data:
            recursive_enumerate(item)
    elif isinstance(node, ValueNode):
        node : ValueNode = node
        path = node.get_full_path()
        
        print(f'{path}:{node.value}')


def draft_node_config():
    config_path = r'test_json/test_data.json'
    
    with open(config_path, 'r') as fh:
        config = json.load(fh)
        
    
    node = DictNode(config, None, None)
    
    
    recursive_enumerate(node)
        
    

if __name__ == '__main__':
    draft_node_config()