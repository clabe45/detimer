from __future__ import annotations
from typing import Dict

import click

from detimer.config import load_config
from detimer.root import Root


instance = None


class App:
	'''The config yaml parsed into something more usable'''

	def __init__(self, roots: Dict[str, Root]) -> None:
		self.roots = roots

	@staticmethod
	def parse(yaml: Dict[str, any]):
		if yaml is None:
			raise click.UsageError('Empty config file')

		try:
			roots = {
				root.name: root for root_yaml in yaml['roots'] if (root := Root.parse(root_yaml))
			}

		except KeyError as e:
			raise click.UsageError(f"Invalid config file (missing property {e})")

		return App(roots)
