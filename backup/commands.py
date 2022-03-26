from typing import List
import click

from backup.app import get_app
from backup.rdiff_backup import RDiffBackupError
from backup.root import Root


@click.group()
def cli():
	pass


@click.group()
def root():
	pass


@click.command(name='list')
def list_roots():
	app = get_app()
	for root in app.roots.values():
		click.echo(f'{root.name}: {root.source} -> {root.destination}')


@click.command()
@click.argument('roots')
def backup(roots: List[str]):
	'''Create a new backup

	Args:
		roots (List[str]): Root names, or '*'

	Raises:
		ValueError: If a root doesn't exit
	'''

	try:
		app = get_app()

		# Get all requested roots from config
		if roots == '*':
			parsed_roots = app.roots.values()
		else:
			parsed_roots = []
			for name in roots:
				if name not in app.roots:
					raise ValueError(f"No such root '{name}'")

				parsed_roots.append(app.roots[name])

		for root in parsed_roots:
			click.echo(f"Backing up '{root.name}'")
			root.backup()

		click.echo('Done')

	except RDiffBackupError as e:
		click.echo(f'rdiff-backup: {e}', err=True)

	except ValueError:
		click.echo(f'backup: {e}', err=True)


def run_command():
	cli()


root.add_command(list_roots)
cli.add_command(root)
cli.add_command(backup)
