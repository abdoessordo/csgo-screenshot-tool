import json


def get_resolution_config(name: str) -> dict:
    with open('./config/resolutions.json', 'r') as resolutions_config_file:
        resolution_configs = json.load(resolutions_config_file)

    return resolution_configs[name]
