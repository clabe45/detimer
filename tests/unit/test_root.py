import pytest

from detimer.matcher import Matcher
from detimer.root import Root, SpecialFileMode


class TestRoot:
    def test_backup_for_root_without_matchers_calls_rdiff_backup(self, mocker):
        rdiff_backup = mocker.patch("detimer.root.rdiff_backup")

        root = Root("foo", "x/foo", "y/foo")
        root.backup()

        rdiff_backup.assert_called_once_with("--verbosity", "3", "x/foo", "y/foo")

    def test_backup_for_root_with_two_matchers_calls_rdiff_backup(self, mocker):
        rdiff_backup = mocker.patch("detimer.root.rdiff_backup")

        root = Root(
            "foo",
            "x/foo",
            "y/foo",
            matchers=[Matcher("a", exclude=True), Matcher("b", exclude=False)],
        )
        root.backup()

        rdiff_backup.assert_called_once_with(
            "--verbosity",
            "3",
            "--exclude",
            "'a'",
            "--include",
            "'b'",
            "x/foo",
            "y/foo",
        )

    def test_backup_for_root_with_special_files_disabled_calls_rdiff_backup(
        self, mocker
    ):
        rdiff_backup = mocker.patch("detimer.root.rdiff_backup")

        root = Root("foo", "x/foo", "y/foo", special_files=SpecialFileMode.EXCLUDE)
        root.backup()

        rdiff_backup.assert_called_once_with(
            "--verbosity", "3", "--exclude-special-files", "x/foo", "y/foo"
        )

    def test_backup_forcefully_calls_rdiff_backup(self, mocker):
        rdiff_backup = mocker.patch("detimer.root.rdiff_backup")

        root = Root("foo", "x/foo", "y/foo")
        root.backup(force=True)

        rdiff_backup.assert_called_once_with(
            "--force", "--verbosity", "3", "x/foo", "y/foo"
        )

    def test_backup_with_verbosity_calls_rdiff_backup(self, mocker):
        rdiff_backup = mocker.patch("detimer.root.rdiff_backup")

        root = Root("foo", "x/foo", "y/foo")
        root.backup(verbosity=0)

        rdiff_backup.assert_called_once_with("--verbosity", "0", "x/foo", "y/foo")

    def test_parse_returns_correct_name(self):
        raw = {"name": "x", "src": "bar", "dest": "foo"}

        root = Root.parse(raw)

        assert root.name == "x"

    def test_parse_returns_correct_source(self):
        raw = {"name": "x", "src": "bar", "dest": "foo"}

        root = Root.parse(raw)

        assert root.source == "bar"

    def test_parse_returns_correct_destination(self):
        raw = {"name": "x", "src": "bar", "dest": "foo"}

        root = Root.parse(raw)

        assert root.destination == "foo"

    def test_parse_with_match_rules_calls_matcher_parse(self, mocker):
        Matcher_parse = mocker.patch("detimer.root.Matcher.parse")

        raw = {
            "name": "x",
            "src": "bar",
            "dest": "foo",
            "match": """+ hello
			- world
			""",
        }

        Root.parse(raw)

        Matcher_parse.assert_has_calls(
            [mocker.call("+ hello", source="bar"), mocker.call("- world", source="bar")]
        )
