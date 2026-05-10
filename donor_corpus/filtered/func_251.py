def main() -> None:
    config = load_config_cli(DEFAULT_ROOT_PATH, 'config.yaml', SERVICE_NAME)
    config['database_path'] = config['simulator_database_path']
    config['peer_db_path'] = config['simulator_peer_db_path']
    config['introducer_peer']['host'] = '127.0.0.1'
    config['introducer_peer']['port'] = 58735
    config['selected_network'] = 'testnet0'
    config['simulation'] = True
    kwargs = service_kwargs_for_full_node_simulator(DEFAULT_ROOT_PATH, config, BlockTools(test_constants))
    return run_service(**kwargs)