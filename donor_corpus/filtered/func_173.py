async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the Glances sensors."""
    client = hass.data[DOMAIN][config_entry.entry_id]
    name = config_entry.data[CONF_NAME]
    dev = []
    for sensor_type, sensor_details in SENSOR_TYPES.items():
        if not sensor_details[0] in client.api.data:
            continue
        if sensor_details[0] in client.api.data:
            if sensor_details[0] == 'fs':
                for disk in client.api.data[sensor_details[0]]:
                    dev.append(GlancesSensor(client, name, disk['mnt_point'], SENSOR_TYPES[sensor_type][1], sensor_type, SENSOR_TYPES[sensor_type]))
            elif sensor_details[0] == 'sensors':
                for sensor in client.api.data[sensor_details[0]]:
                    dev.append(GlancesSensor(client, name, sensor['label'], SENSOR_TYPES[sensor_type][1], sensor_type, SENSOR_TYPES[sensor_type]))
            elif client.api.data[sensor_details[0]]:
                dev.append(GlancesSensor(client, name, '', SENSOR_TYPES[sensor_type][1], sensor_type, SENSOR_TYPES[sensor_type]))
    async_add_entities(dev, True)