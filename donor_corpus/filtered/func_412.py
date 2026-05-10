def test_repo_context_success(file_config_files, capsys):
    expected_rev = testing.git.revparse(file_config_files.dir1)
    with autofix_lib.repo_context(str(file_config_files.output_dir.join('repo1')), use_color=False):
        assert testing.git.revparse('.') == expected_rev
        assert git.remote('.') == file_config_files.dir1
    out, err = capsys.readouterr()
    assert err == ''
    assert 'Errored' not in out