import pytest

from detimer.commands import backup


def test_backup_with_no_roots_prints_help_message_and_aborts():
    with pytest.raises(SystemExit):
        backup()
