from __future__ import annotations
from typing import Dict
from backup.config import load_config

from backup.root import Root


instance = None


class App:
	def __init__(self, roots: Dict[str, Root]) -> None:
		self.roots = roots

	@staticmethod
	def parse(yaml: Dict[str, any]):
		roots = [Root.parse(root_yaml) for root_yaml in yaml['roots']]

		return App(roots)


def get_app():
	global instance

	if instance is None:
		yaml = load_config()
		instance = App.parse(yaml)

	return instance