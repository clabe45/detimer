from __future__ import annotations
from typing import Any, Dict, List

from backup.matcher import Matcher


class Root:
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
			matchers = [Matcher.parse(matcher.strip()) for matcher in matchers]
		else:
			matchers = None

		return Root(name, src, dest, matchers)
