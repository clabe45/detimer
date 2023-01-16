def test_backup_with_default_config_file_has_exit_code_of_zero(run, no_config):
    result = run("backup", "-a")

    assert result.exit_code == 0


def test_backup_with_default_config_file_outputs_done(run, no_config):
    result = run("backup", "-a")

    assert result.output == "Done\n"


def test_backup_with_no_roots_prints_help_message_and_aborts(run, no_config):
    result = run("backup")

    assert "Usage: cli backup [OPTIONS] [ROOTS]..." in result.output


def test_backup_with_force_and_all_confirms(run, no_config):
    result = run("backup", "-a", "-f")

    assert "Are you sure you want to force all backups?" in result.output
