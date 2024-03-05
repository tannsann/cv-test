from datetime import datetime, timedelta
import yfinance as yf
import pytz
import logging
import os
import pandas as pd

import sys
project_relative_dir = "../../../"
sys.path.append(project_relative_dir)

from src.libs.configs import inject_shared_configs, load_shared_config

cfg = load_shared_config()

@inject_shared_configs
def debug_info(logger: logging.Logger, msg: str, debug: bool):
    
    if debug:
        logger.info(msg)

