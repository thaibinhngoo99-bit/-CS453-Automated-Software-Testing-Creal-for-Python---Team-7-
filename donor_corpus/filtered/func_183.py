def test_export_codegen(rule_runner: RuleRunner) -> None:
    rule_runner.add_to_build_file('', "gen1(name='gen1')\ngen2(name='gen2')\n")
    result = rule_runner.run_goal_rule(ExportCodegen, args=['::'])
    assert result.exit_code == 0
    parent_dir = Path(rule_runner.build_root, 'dist', 'codegen')
    assert (parent_dir / 'assets' / 'README.md').read_text() == 'Hello!'
    assert (parent_dir / 'src' / 'haskell' / 'app.hs').read_text() == '10 * 4'