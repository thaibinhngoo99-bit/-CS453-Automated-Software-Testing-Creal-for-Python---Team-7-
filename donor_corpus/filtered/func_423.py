def test_fix_with_limit(file_config_files, capfd):
    autofix_lib.fix((str(file_config_files.output_dir.join('repo1')), str(file_config_files.output_dir.join('repo2'))), apply_fix=lower_case_f, config=load_config(file_config_files.cfg), commit=autofix_lib.Commit('message!', 'test-branch', None), autofix_settings=autofix_lib.AutofixSettings(jobs=1, color=False, limit=1, dry_run=True, interactive=False))
    out, err = capfd.readouterr()
    assert err == ''
    assert 'Errored' not in out
    assert '-OHAI\n+ohai\n' in out
    assert '-OHELLO\n+ohello\n' not in out