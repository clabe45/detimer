from typing import List

import click

from detimer.app import App
from detimer.rdiff_backup import RDiffBackupError


def backup(app: App, all_: bool, force: bool, verbosity: int, roots: List[str]):
    """
    Backup specified roots

    Creates a new backup for each specified root. One or more root names can be
    included.
    """

    if force and all_:
        if not click.confirm("Are you sure you want to force all backups?"):
            if verbosity > 0:
                click.echo("Aborting")

            return

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
                    # click.BadParameter adds too many words to the error
                    # message, so I'm using click.UsageError
                    raise click.UsageError(f"No such root '{name}'")

                parsed_roots.append(app.roots[name])

        for root in parsed_roots:
            if verbosity > 0:
                click.echo(f"Backing up '{root.name}'")

            root.backup(force=force, verbosity=verbosity)

        if verbosity > 0:
            click.echo("Done")

    except RDiffBackupError as e:
        click.echo(f"rdiff-backup error: {e}", err=True)


def list_(app: App):
    """List all roots"""

    for root in app.roots.values():
        click.echo(f"* {root.name} ({root.source} -> {root.destination})")
