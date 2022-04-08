from typing import List

import click

from detimer.app import App
from detimer.config import load_config
from detimer.constants import VERSION
from detimer.rdiff_backup import RDiffBackupError
from detimer.root import Root

CONTEXT_SETTINGS = {
	'help_option_names': ['-h', '--help']
}


@click.group(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.version_option(VERSION, '-V', '--version')
def cli(ctx: click.Context):
	'''Universal backup manager'''

	config = load_config()
	ctx.obj = App.parse(config)


@click.command()
@click.pass_obj
@click.option('-a', '--all', 'all_', is_flag=True)
@click.argument('roots', required=False, nargs=-1)
def backup(app: App, all_: bool, roots: List[str]):
	'''
	Backup specified roots

	Creates a new backup for each specified root. One or more root names can be
	included.
	'''

	try:
		# Get all requested roots from config
		if all_:
			parsed_roots = app.roots.values()
		else:
			if len(roots) == 0:
				# Print help message and abort
				ctx = click.get_current_context()
				click.echo(ctx.get_help())
				ctx.exit()

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

	except ValueError as e:
		click.echo(f'backup: {e}', err=True)


@click.command(name='list')
@click.pass_obj
def list_(app: App):
	'''List all roots'''

	for root in app.roots.values():
		click.echo(f'* {root.name} ({root.source} -> {root.destination})')


def run_command():
	cli()


cli.add_command(backup)
cli.add_command(list_)
