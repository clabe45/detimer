from __future__ import annotations
import os

from click import get_app_dir
from yaml import Loader, load

from backup.constants import APP_NAME


PATH = os.path.join(get_app_dir(APP_NAME), 'config.yml')


def load_config():
	with open(PATH, 'r') as f:
		return load(f.read(), Loader=Loader)
