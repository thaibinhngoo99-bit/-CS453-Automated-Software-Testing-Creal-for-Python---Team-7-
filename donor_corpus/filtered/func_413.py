def test_repo_context_errors(file_config_files, capsys):
    with autofix_lib.repo_context(str(file_config_files.output_dir.join('repo1')), use_color=False):
        assert False
    out, err = capsys.readouterr()
    assert 'Errored' in out
    assert 'assert False' in err