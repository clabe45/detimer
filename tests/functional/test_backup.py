def test_backup_with_default_config_file_has_exit_code_of_zero(run, no_config):
    result = run("backup", "-a")

    assert result.exit_code == 0


def test_backup_with_default_config_file_outputs_done(run, no_config):
    result = run("backup", "-a")

    assert result.output == "Done\n"
