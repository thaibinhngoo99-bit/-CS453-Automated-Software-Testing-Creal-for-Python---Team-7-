def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the Supervisord platform."""
    url = config.get(CONF_URL)
    try:
        supervisor_server = xmlrpc.client.ServerProxy(url)
        processes = supervisor_server.supervisor.getAllProcessInfo()
    except ConnectionRefusedError:
        _LOGGER.error('Could not connect to Supervisord')
        return False
    add_entities([SupervisorProcessSensor(info, supervisor_server) for info in processes], True)