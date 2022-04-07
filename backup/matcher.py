from __future__ import annotations


class Matcher:
	def __init__(self, pattern: str, exclude = False) -> None:
		self.pattern = pattern
		self.exclude = exclude

	@staticmethod
	def parse(line) -> Matcher:
		# Each line (pattern) takes one of the following forms:
		# + path/to/include
		# - path/to-exclude

		line = line.strip()

		if not line.startswith('+') and not line.startswith('-'):
			raise ValueError("Each pattern must begin with '+' or '-'")

		exclude = line.startswith('-')
		pattern = line[1:].strip()
		return Matcher(pattern, exclude)
