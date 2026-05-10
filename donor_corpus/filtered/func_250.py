def service_kwargs_for_full_node_simulator(root_path: Path, config: Dict, bt: BlockTools) -> Dict:
    mkdir(path_from_root(root_path, config['database_path']).parent)
    constants = bt.constants
    node = FullNode(config, root_path=root_path, consensus_constants=constants, name=SERVICE_NAME)
    peer_api = FullNodeSimulator(node, bt)
    network_id = config['selected_network']
    kwargs = dict(root_path=root_path, node=node, peer_api=peer_api, node_type=NodeType.FULL_NODE, advertised_port=config['port'], service_name=SERVICE_NAME, server_listen_ports=[config['port']], on_connect_callback=node.on_connect, rpc_info=(FullNodeRpcApi, config['rpc_port']), network_id=network_id)
    return kwargs