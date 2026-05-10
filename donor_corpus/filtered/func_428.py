def test_fix_non_default_branch(file_config_non_default):
    clone.main(('--config-filename', str(file_config_non_default.cfg)))
    autofix_lib.fix((str(file_config_non_default.output_dir.join('repo1')),), apply_fix=lower_case_f, config=load_config(file_config_non_default.cfg), commit=autofix_lib.Commit('message!', 'test-branch', 'A B <a@a.a>'), autofix_settings=autofix_lib.AutofixSettings(jobs=1, color=False, limit=None, dry_run=False, interactive=False))
    assert file_config_non_default.dir1.join('f').read() == 'ohai\n'