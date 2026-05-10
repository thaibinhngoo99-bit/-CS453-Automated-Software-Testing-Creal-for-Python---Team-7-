def _get_group_data(deploy_dir):
    group_data = {}
    group_data_directory = path.join(deploy_dir, 'group_data')
    if path.exists(group_data_directory):
        files = listdir(group_data_directory)
        for file in files:
            if not file.endswith('.py'):
                continue
            group_data_file = path.join(group_data_directory, file)
            group_name = path.basename(file)[:-3]
            logger.debug('Looking for group data in: {0}'.format(group_data_file))
            attrs = exec_file(group_data_file, return_locals=True)
            group_data[group_name] = {key: value for key, value in six.iteritems(attrs) if _is_group_data(key, value)}
    return group_data