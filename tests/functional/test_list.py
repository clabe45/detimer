import os

from click.testing import CliRunner
import pytest

from detimer.config import CONFIG_DIR


def test_list_with_no_config_file_has_exit_code_of_zero(run, no_config):
    result = run("list")

    assert result.exit_code == 0


def test_list_with_no_config_file_outputs_nothing(run, no_config):
    result = run("list")

    assert len(result.output) == 0
