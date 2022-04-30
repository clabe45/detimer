from __future__ import annotations
import importlib.resources
import os

from click import get_app_dir
from yaml import Loader, load

from detimer.constants import APP_NAME


CONFIG_DIR = get_app_dir(APP_NAME)
CONFIG_FILE = os.path.join(CONFIG_DIR, 'config.yml')


def load_config():
	if not os.path.exists(CONFIG_DIR):
		os.mkdir(CONFIG_DIR)
	elif not os.path.isdir(CONFIG_DIR):
		raise Exception(f'{CONFIG_DIR} is not a directory')

	if not os.path.exists(CONFIG_FILE):
		with (
			open(CONFIG_FILE, 'w+') as real,
			importlib.resources.open_text('detimer.data', 'default-config.yml') as default
		):
			default_config = default.read()
			real.write(default_config)

	elif not (os.path.isfile(CONFIG_FILE) or os.path.islink(CONFIG_FILE)):
		raise Exception(f'{CONFIG_FILE} must be a file or a symlink')

	with open(CONFIG_FILE, 'r') as f:
		return load(f.read(), Loader=Loader)
