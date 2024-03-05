import sys
from functools import wraps
from inspect import signature

project_relative_dir = "../../../"
sys.path.append(project_relative_dir)

from src.configs.shared_config import SHARED_CONFIG

def load_shared_config():

    shared_config = SHARED_CONFIG.copy()

    return shared_config

cfg = load_shared_config()

def inject_shared_configs(func):
    """
    Decorator to inject key values in .../configs/shared_config.py into function call args
    """
    func._params = list(signature(func).parameters.keys())

    @wraps(func)
    def _wrapper(*args, **kwargs):
        for param_name in func._params[len(args):]:
            if param_name not in kwargs and param_name in cfg:
                kwargs[param_name] = cfg[param_name]

        return func(*args, **kwargs)

    return _wrapper
