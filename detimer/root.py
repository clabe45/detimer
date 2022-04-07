from __future__ import annotations
from typing import Any, Dict, List

from detimer.matcher import Matcher
from detimer.rdiff_backup import rdiff_backup


class Root:
	'''Backup job'''

	def __init__(
		self,
		name: str,
		source: str,
		destination: str,
		matchers: List[Matcher] = None
	) -> None:
		if matchers is None:
			matchers = []

		self.name = name
		self.source = source
		self.destination = destination
		self.matchers = matchers

	def backup(self) -> None:
		matcher_args = [arg for matcher in self.matchers for arg in ['--exclude' if matcher.exclude else '--include', f"'{matcher.pattern}'"]]
		rdiff_backup(*matcher_args, self.source, self.destination)

	@staticmethod
	def parse(yaml: Dict[str, Any]) -> Root:
		'''Parse from yaml entry for this root in the user's config'''

		if not isinstance(yaml, dict):
			raise TypeError('Root yaml must be a dictionary')

		if 'name' not in yaml:
			raise ValueError("Each root must have a 'name'")

		if 'src' not in yaml or 'dest' not in yaml:
			raise ValueError("Each root must have 'src' and 'dest' paths")

		name = yaml['name']
		src = yaml['src']
		dest = yaml['dest']

		if 'match' in yaml:
			matchers = yaml['match'].strip().split('\n')
			matchers = [Matcher.parse(matcher.strip(), source=src) for matcher in matchers]
		else:
			matchers = None

		return Root(name, src, dest, matchers)
