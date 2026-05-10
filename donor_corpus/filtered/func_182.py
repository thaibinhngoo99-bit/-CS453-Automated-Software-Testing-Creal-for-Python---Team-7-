def test_no_codegen_targets(rule_runner: RuleRunner, caplog) -> None:
    result = rule_runner.run_goal_rule(ExportCodegen)
    assert result.exit_code == 0
    assert len(caplog.records) == 1
    assert 'No codegen files/targets matched. All codegen target types: gen1, gen2' in caplog.text