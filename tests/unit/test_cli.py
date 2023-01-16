def test_backup_calls_backup_command(mocker, run):
    backup = mocker.patch("detimer.cli.commands.backup")
    run("backup", "-f", "-v0", "root1", "root2")

    backup.assert_called_once_with(mocker.ANY, False, True, 0, ("root1", "root2"))
