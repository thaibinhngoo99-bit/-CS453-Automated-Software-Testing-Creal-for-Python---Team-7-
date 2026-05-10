def test_noop_does_not_commit(file_config_files):
    rev_before1 = testing.git.revparse(file_config_files.dir1)
    rev_before2 = testing.git.revparse(file_config_files.dir2)
    autofix_lib.fix((str(file_config_files.output_dir.join('repo1')), str(file_config_files.output_dir.join('repo2'))), apply_fix=lambda: None, config=load_config(file_config_files.cfg), commit=autofix_lib.Commit('message!', 'test-branch', None), autofix_settings=autofix_lib.AutofixSettings(jobs=1, color=False, limit=None, dry_run=False, interactive=False))
    rev_after1 = testing.git.revparse(file_config_files.dir1)
    rev_after2 = testing.git.revparse(file_config_files.dir2)
    assert (rev_before1, rev_before2) == (rev_after1, rev_after2)