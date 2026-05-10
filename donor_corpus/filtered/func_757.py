def get_deploy_order(contracts_to_deploy, compiled_contracts):
    dependency_graph = compute_direct_dependency_graph(compiled_contracts.values())
    global_deploy_order = compute_deploy_order(dependency_graph)
    all_deploy_dependencies = set(itertools.chain.from_iterable((compute_recursive_contract_dependencies(contract_name, dependency_graph) for contract_name in contracts_to_deploy)))
    all_contracts_to_deploy = all_deploy_dependencies.union(contracts_to_deploy)
    deploy_order = tuple((contract_name for contract_name in global_deploy_order if contract_name in all_contracts_to_deploy))
    return deploy_order