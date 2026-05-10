def setup_platform(hass, config, add_entities, _=None):
    """Set up the ICS Calendar platform"""
    _LOGGER.debug('Setting up ics calendars')
    calendar_devices = []
    for calendar in config.get(CONF_CALENDARS):
        device_data = {CONF_NAME: calendar.get(CONF_NAME), CONF_URL: calendar.get(CONF_URL), CONF_INCLUDE_ALL_DAY: calendar.get(CONF_INCLUDE_ALL_DAY), CONF_USERNAME: calendar.get(CONF_USERNAME), CONF_PASSWORD: calendar.get(CONF_PASSWORD), CONF_PARSER: calendar.get(CONF_PARSER)}
        device_id = '{}'.format(device_data[CONF_NAME])
        entity_id = generate_entity_id(ENTITY_ID_FORMAT, device_id, hass=hass)
        calendar_devices.append(ICSCalendarEventDevice(entity_id, device_data))
    add_entities(calendar_devices)