from __future__ import annotations
import os
from typing import Dict, List

from click import get_app_dir
from backup.root import Root
from yaml import Loader, load

from backup.constants import APP_NAME


PATH = os.path.join(get_app_dir(APP_NAME), 'config.yml')


instance = None


def _load_yaml():
	with open(PATH, 'r') as f:
		return load(f.read(), Loader=Loader)


def get_config():
	global instance

	if instance is None:
		yaml = _load_yaml()
		instance = Config.parse(yaml)

	return instance


class Config:
	def __init__(self, roots: List[Root]) -> None:
		self.roots = roots

	@staticmethod
	def parse(yaml: Dict[str, any]):
		roots = [Root.parse(root_yaml) for root_yaml in yaml['roots']]
		return Config(roots)
