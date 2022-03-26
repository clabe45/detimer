import subprocess
from typing import List

import click


class RDiffBackupError(Exception):
	pass


def rdiff_backup(*args: List[str]) -> None:
	p = subprocess.Popen(['rdiff-backup'] + list(args), stderr=subprocess.PIPE, text=True)
	_, stderr = p.communicate()

	if p.returncode != 0:
		raise RDiffBackupError(stderr)

	elif stderr:
		click.echo(f'rdiff-backup: {stderr}', err=True)
