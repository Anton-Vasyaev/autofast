import dependencies
# 3rd party
import ganymede.json as g_json
# project
from fastdi.config import deserialize_config

from test_data.training_configuration import TrainingConfiguration


config_path = 'test_json/test_data.json'
config      = g_json.load_from_file(config_path)

train_configuration : TrainingConfiguration = deserialize_config(TrainingConfiguration, config)

print(train_configuration)