def test_autofix_makes_commits(file_config_files, capfd):
    autofix_lib.fix((str(file_config_files.output_dir.join('repo1')), str(file_config_files.output_dir.join('repo2'))), apply_fix=lower_case_f, config=load_config(file_config_files.cfg), commit=autofix_lib.Commit('message!', 'test-branch', 'A B <a@a.a>'), autofix_settings=autofix_lib.AutofixSettings(jobs=1, color=False, limit=None, dry_run=False, interactive=False))
    out, err = capfd.readouterr()
    assert err == ''
    assert 'Errored' not in out
    assert file_config_files.dir1.join('f').read() == 'ohai\n'
    assert file_config_files.dir2.join('f').read() == 'ohello\n'
    last_commit_msg = subprocess.check_output(('git', '-C', file_config_files.dir1, 'log', '--format=%s', '--first-parent', '-1')).decode()
    assert last_commit_msg == "Merge branch 'all-repos_autofix_test-branch'\n"
    commit = subprocess.check_output(('git', '-C', file_config_files.dir1, 'log', '--patch', '--grep', 'message!', '--format=%an %ae\n%B')).decode()
    assert commit.startswith('A B a@a.a\nmessage!\n\nCommitted via https://github.com/asottile/all-repos\n')
    assert commit.endswith('-OHAI\n+ohai\n')