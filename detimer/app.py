from __future__ import annotations
from typing import Dict
from detimer.config import load_config

from detimer.root import Root


instance = None


class App:
	'''The config yaml parsed into something more usable'''

	def __init__(self, roots: Dict[str, Root]) -> None:
		self.roots = roots

	@staticmethod
	def parse(yaml: Dict[str, any]):
		roots = {
			root.name: root for root_yaml in yaml['roots'] if (root := Root.parse(root_yaml))
		}

		return App(roots)


def get_app():
	global instance

	if instance is None:
		yaml = load_config()
		instance = App.parse(yaml)

	return instance
