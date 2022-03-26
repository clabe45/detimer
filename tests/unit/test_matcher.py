import pytest

from backup.matcher import Matcher


class TestMatcher:
	def test_parse_with_include_line_returns_correct_type(self):
		matcher = Matcher.parse('+ foo', 'a')
		assert not matcher.exclude

	def test_parse_with_exclude_line_returns_correct_type(self):
		matcher = Matcher.parse('- foo', 'a')
		assert matcher.exclude

	def test_parse_with_relative_path_returns_correct_pattern(self):
		matcher = Matcher.parse('+ foo', 'a')
		assert matcher.pattern == 'a/foo'

	def test_parse_with_absolute_path_returns_correct_pattern(self):
		matcher = Matcher.parse('+ /foo', 'a')
		assert matcher.pattern == '/foo'
