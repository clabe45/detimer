from __future__ import annotations
import os


class Matcher:
	'''Inclusion/exclusion rule'''

	def __init__(self, pattern: str, exclude = False) -> None:
		self.pattern = pattern
		self.exclude = exclude

	@staticmethod
	def parse(line: str, source: str) -> Matcher:
		# Each line (pattern) takes one of the following forms:
		# + path/to/include
		# - path/to-exclude

		line = line.strip()

		if not line.startswith('+') and not line.startswith('-'):
			raise ValueError("Each pattern must begin with '+' or '-'")

		exclude = line.startswith('-')
		pattern = line[1:].strip()

		# If it's a relative path, prepend the base source path, because
		# rdiff-backup doesn't support relative paths
		if not pattern.startswith(os.path.sep):
			pattern = os.path.join(source, pattern)

		return Matcher(pattern, exclude)
