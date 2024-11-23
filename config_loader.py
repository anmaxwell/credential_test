import json
import os

class ConfigLoader:
    _config = None

    @staticmethod
    def get_config():
        """Loads the JSON config file as a singleton."""
        if ConfigLoader._config is None:
            config_path = os.getenv('CONFIG_PATH', 'credentials.json')  # Allow for dynamic paths
            with open(config_path, 'r') as f:
                ConfigLoader._config = json.load(f)
        return ConfigLoader._config
