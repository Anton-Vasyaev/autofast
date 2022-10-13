import dependencies
# test
from fastdi.config import deserialize_config
# python
import json
# project
from test_data.training_configuration import TrainingConfiguration
from test_data.image_type             import ImageType
from test_data.aug_distributions      import StretchImageType, StretchOrientationType


def float_equal(val, rel_eps = 1e-6):
    abs_eps = val * rel_eps
    
    min_v = val - abs_eps
    max_v = val + abs_eps
    
    return min_v < val and val < max_v


def float_tuple_equal(t1, t2):
    for el1, el2 in zip(t1, t2):
        if not float_equal(el1, el2):
            return False
    
    return True
    

def test_basic_deserialization():
    json_path = 'resources/test_data.json'
    
    with open(json_path, 'r') as fh:
        config = json.load(fh)
        
    configuration = deserialize_config(TrainingConfiguration, config)
    
    print(configuration)
    
    # Check TrainingParameters
    train_params = configuration.train_params
    
    assert train_params.input_size == (1024, 512)
    assert train_params.image_type == ImageType.BGRA
    assert train_params.batch_size == 8
    assert float_equal(train_params.learning_rate, 0.001) 
    assert train_params.use_gpu == True
    
    
    # Check EnvironmentSettings
    env_sets = configuration.env_settings
    assert env_sets.checkpoint_path == 'path/to/checkpoint/dir'
    assert env_sets.export_path == 'path/to/export/dir'
    
    models = [
        ("EfficientNet",         23, True),

        ("BobaBibaNet-12",       53, False),

        ("SpipuchkinModel-256", 241, True)
    ]

    assert env_sets.models == models
    
    # Check AugParams
    aug_params = configuration.aug_params
    
    aug_dist = aug_params.aug_dist
    
    # BasiColorDistribution
    basic_color = aug_dist.basic_color
    assert float_tuple_equal(basic_color.red,   [0.6, 1.6])
    assert float_tuple_equal(basic_color.green, [0.73, 1.234])
    assert float_tuple_equal(basic_color.green, [0.81, 1.1])

    rotate3d = aug_dist.rotate_3d
    assert float_tuple_equal(rotate3d.angles, [0.321, -0.56, 2.0])
    
    mirror = aug_dist.mirror
    assert float_equal(mirror.horizontal, 0.85)
    assert float_equal(mirror.vertical,   0.13)
    
    stretch = aug_dist.stretch
    assert stretch.orientation == StretchOrientationType.VERTICAL
    assert stretch.image       == StretchImageType.DST
    
    assert float_equal(aug_params.aug_size, 3.65)
    
    assert configuration.module_name is None