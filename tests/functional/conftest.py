import os

from click.testing import CliRunner
import pytest

from detimer.commands import cli
from detimer.config import CONFIG_DIR


@pytest.fixture()
def run():
    runner = CliRunner()

    def invoke(*args):
        return runner.invoke(cli, args, catch_exceptions=False)

    return invoke


@pytest.fixture()
def no_config(fs):
    parent_dir = os.path.dirname(CONFIG_DIR)

    # Create top-level configuration directory (e.g. ~/.config)
    fs.create_dir(parent_dir)

    # Copy default config file to fake file system
    fs.add_real_file("detimer/data/default-config.yml")
