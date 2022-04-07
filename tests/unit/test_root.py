from backup.root import Root
import pytest

from backup.root import Root


class TestRoot:
	def test_parse_returns_correct_source(self):
		raw = {
			'src': 'bar',
			'dest': 'foo'
		}

		root = Root.parse(raw)

		assert root.source == 'bar'

	def test_parse_returns_correct_destination(self):
		raw = {
			'src': 'bar',
			'dest': 'foo'
		}

		root = Root.parse(raw)

		assert root.destination == 'foo'

	def test_parse_with_match_rules_calls_matcher_parse(self, mocker):
		Matcher_parse = mocker.patch('backup.matcher.Matcher.parse')

		raw = {
			'src': 'bar',
			'dest': 'foo',
			'match': '''+ hello
			- world
			'''
		}

		Root.parse(raw)

		Matcher_parse.assert_has_calls([
			mocker.call('+ hello'),
			mocker.call('- world')
		])
