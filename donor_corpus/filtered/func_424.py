def test_fix_interactive(file_config_files, capfd, mock_input):
    mock_input.set_side_effect('y', 'n')
    autofix_lib.fix((str(file_config_files.output_dir.join('repo1')), str(file_config_files.output_dir.join('repo2'))), apply_fix=lower_case_f, config=load_config(file_config_files.cfg), commit=autofix_lib.Commit('message!', 'test-branch', None), autofix_settings=autofix_lib.AutofixSettings(jobs=1, color=False, limit=None, dry_run=False, interactive=True))
    assert file_config_files.dir1.join('f').read() == 'ohai\n'
    assert file_config_files.dir2.join('f').read() == 'OHELLO\n'