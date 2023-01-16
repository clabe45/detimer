from click.testing import CliRunner
import pytest

from detimer.cli import cli


@pytest.fixture()
def run():
    runner = CliRunner()

    def invoke(*args):
        return runner.invoke(cli, args, catch_exceptions=False)

    return invoke
