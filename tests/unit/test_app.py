import pytest

from detimer.app import App


class TestApp:
    def test_parse_with_one_root_calls_root_parse(self, mocker):
        Root_parse = mocker.patch("detimer.app.Root.parse")

        raw_root = {
            "name": "x",
            "src": "bar",
            "dest": "foo",
            "special_files": "include",
            "match": """+ hello
			- world
			""",
        }

        raw_app = {"roots": [raw_root]}

        App.parse(raw_app)

        Root_parse.assert_called_once_with(raw_root)
