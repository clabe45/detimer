import click

from backup.config import get_config


@click.group()
def cli():
	pass


@click.group()
def root():
	pass


@click.command(name='list')
def list_roots():
	conf = get_config()
	for root in conf.roots:
		click.echo(f'{root.source} -> {root.destination}')


def run_command():
	cli()


root.add_command(list_roots)
cli.add_command(root)
