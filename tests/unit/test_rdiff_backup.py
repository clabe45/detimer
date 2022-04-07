import subprocess
import pytest

from detimer.rdiff_backup import rdiff_backup


class TestRDiffBackup:
	def test_rdiff_backup_calls_subprocess_Popen(self, mocker):
		p = subprocess.Popen(['echo'])
		Popen = mocker.patch('detimer.rdiff_backup.subprocess.Popen', return_value=p)

		rdiff_backup('a', 'b', 'c')

		Popen.assert_called_once_with('rdiff-backup a b c', universal_newlines=True, stderr=subprocess.PIPE, shell=True, text=True)
