from typing import List

import click

from detimer import commands
from detimer.app import App
from detimer.config import load_config
from detimer.constants import VERSION
from detimer.rdiff_backup import RDiffBackupError
from detimer.root import Root

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}


@click.group(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.version_option(VERSION, "-V", "--version")
def cli(ctx: click.Context):
    """Supercharged rdiff-backup wrapper"""

    config = load_config()
    ctx.obj = App.parse(config)


@click.command()
@click.pass_obj
@click.option("-a", "--all", "all_", is_flag=True)
@click.option("-f", "--force", is_flag=True)
@click.option("-v", "--verbosity", type=click.IntRange(0, 9), default=3, show_default=True)
@click.argument("roots", required=False, nargs=-1)
def backup(app: App, all_: bool, force: bool, verbosity: int, roots: List[str]):
    """
    Backup specified roots

    Creates a new backup for each specified root. One or more root names can be
    included.
    """

    commands.backup(app, all_, force, verbosity, roots)


@click.command(name="list")
@click.pass_obj
def list_(app: App):
    """List all roots"""

    commands.list_(app)


def run_command():
    cli()


cli.add_command(backup)
cli.add_command(list_)
