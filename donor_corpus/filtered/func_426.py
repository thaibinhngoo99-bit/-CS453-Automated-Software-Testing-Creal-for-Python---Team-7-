def test_fix_failing_check_no_changes(file_config_files, capfd):
    autofix_lib.fix((str(file_config_files.output_dir.join('repo1')), str(file_config_files.output_dir.join('repo2'))), apply_fix=lower_case_f, check_fix=failing_check_fix, config=load_config(file_config_files.cfg), commit=autofix_lib.Commit('message!', 'test-branch', None), autofix_settings=autofix_lib.AutofixSettings(jobs=1, color=False, limit=None, dry_run=False, interactive=False))
    out, err = capfd.readouterr()
    assert 'nope!' in err
    assert out.count('Errored') == 2
    assert file_config_files.dir1.join('f').read() == 'OHAI\n'
    assert file_config_files.dir2.join('f').read() == 'OHELLO\n'