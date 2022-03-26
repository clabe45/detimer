import pytest

from backup.matcher import Matcher
from backup.root import Root


class TestRoot:
	def test_backup_for_root_without_matchers_calls_rdiff_backup(self, mocker):
		rdiff_backup = mocker.patch('backup.root.rdiff_backup')

		root = Root('foo', 'x/foo', 'y/foo')
		root.backup()

		rdiff_backup.assert_called_once_with('x/foo', 'y/foo')

	def test_backup_for_root_with_two_matchers_calls_rdiff_backup(self, mocker):
		rdiff_backup = mocker.patch('backup.root.rdiff_backup')

		root = Root('foo', 'x/foo', 'y/foo', [
			Matcher('a', exclude=True),
			Matcher('b', exclude=False)
		])
		root.backup()

		rdiff_backup.assert_called_once_with('--exclude', 'a', '--include', 'b', 'x/foo', 'y/foo')

	def test_parse_returns_correct_name(self):
		raw = {
			'name': 'x',
			'src': 'bar',
			'dest': 'foo'
		}

		root = Root.parse(raw)

		assert root.name == 'x'

	def test_parse_returns_correct_source(self):
		raw = {
			'name': 'x',
			'src': 'bar',
			'dest': 'foo'
		}

		root = Root.parse(raw)

		assert root.source == 'bar'

	def test_parse_returns_correct_destination(self):
		raw = {
			'name': 'x',
			'src': 'bar',
			'dest': 'foo'
		}

		root = Root.parse(raw)

		assert root.destination == 'foo'

	def test_parse_with_match_rules_calls_matcher_parse(self, mocker):
		Matcher_parse = mocker.patch('backup.root.Matcher.parse')

		raw = {
			'name': 'x',
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
