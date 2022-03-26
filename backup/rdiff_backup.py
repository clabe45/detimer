import subprocess
from typing import List


class RDiffBackupError(Exception):
	pass


def rdiff_backup(*args: List[str]) -> None:
	p = subprocess.Popen(['rdiff-backup'] + list(args), stderr=subprocess.PIPE)
	_, stderr = p.communicate()
	if p.returncode != 0:
		raise RDiffBackupError(stderr)
