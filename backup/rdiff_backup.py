import subprocess
from typing import List

import click


class RDiffBackupError(Exception):
	pass


def rdiff_backup(*args: List[str]) -> None:
	# The command has to be a string, not a list, because some arguments
	# contains single quotes.
	cmd = ' '.join(['rdiff-backup'] + list(args))
	p = subprocess.Popen(cmd, universal_newlines=True, stderr=subprocess.PIPE, shell=True, text=True)
	_, stderr = p.communicate()

	if p.returncode != 0:
		raise RDiffBackupError(stderr)

	elif stderr:
		click.echo(f'rdiff-backup: {stderr}', err=True)
