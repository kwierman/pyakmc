import logging
import os
from collections import defaultdict
from typing import Any

import yaml
from dotenv import load_dotenv

load_dotenv()


_global_config_dict = defaultdict(None)


class Configuration:
    """

    Order of config overrides:
     1. Defaults internal to classes that inherit from this class
     2. Environment variables
     3. Files from .env (please avoid)
     4. Yaml files
        1. Includes are declared first
        2. Overrides come from parent files

    """

    logger = logging.getLogger("")

    def __init__(self):
        self._internal = _global_config_dict

    def configure(self, filename):

        self.configure_from_environment()
        config = self.config_yaml(filename)
        self._internal.update(config)

    def configure_from_environment(self):
        for key in self._internal.keys():
            if key in os.environ.keys():
                self._internal[key] = os.environ.get(key)

    def get(self, key) -> Any:
        return self._internal[key]

    def config_yaml(self, filename: str):
        config = defaultdict(None)
        top_level_config = self.load_yaml(filename)
        if "include" in top_level_config.keys():
            if isinstance(top_level_config["include"], list):
                for item in top_level_config["include"]:
                    config.update(self.config_yaml(item))
            elif isinstance(top_level_config["include"], str):
                config.update(self.config_yaml(item))
            del config["include"]
        config.update(top_level_config)
        return config

    def load_yaml(self, filename: str):
        with open(filename) as _file:
            return yaml.safe_load(_file)
