from detimer.app import App
from detimer.commands import backup


def test_backup_calls_backup_on_each_root(mocker, click, app: App):
    backup(app, all_=False, force=False, verbosity=0, roots=app.roots)

    for root in app.roots.values():
        root.backup.assert_called_once_with(force=False, verbosity=0)
