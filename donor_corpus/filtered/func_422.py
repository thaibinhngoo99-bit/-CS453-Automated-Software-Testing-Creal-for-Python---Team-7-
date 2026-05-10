def test_fix_dry_run_no_change(file_config_files, capfd):
    autofix_lib.fix((str(file_config_files.output_dir.join('repo1')), str(file_config_files.output_dir.join('repo2'))), apply_fix=lower_case_f, config=load_config(file_config_files.cfg), commit=autofix_lib.Commit('message!', 'test-branch', None), autofix_settings=autofix_lib.AutofixSettings(jobs=1, color=False, limit=None, dry_run=True, interactive=False))
    out, err = capfd.readouterr()
    assert err == ''
    assert 'Errored' not in out
    assert '-OHAI\n+ohai\n' in out
    assert '-OHELLO\n+ohello\n' in out
    assert file_config_files.dir1.join('f').read() == 'OHAI\n'
    assert file_config_files.dir2.join('f').read() == 'OHELLO\n'