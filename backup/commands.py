from typing import List
import click

from backup.app import get_app
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


def run_command():
	cli()


root.add_command(list_roots)
cli.add_command(root)
