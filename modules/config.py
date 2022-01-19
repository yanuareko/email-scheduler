import yaml


def load_config(filename: str) -> dict:
    dict_data: dict = {}
    with open(filename) as stream_config:
        try:
            dict_data: dict = yaml.safe_load(stream_config)
        except yaml.YAMLError as exc:
            print("yaml.YAMLError: %s" % exc)
    return dict_data
