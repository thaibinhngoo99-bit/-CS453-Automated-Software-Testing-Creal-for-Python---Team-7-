def read_config_from_github(sdk_id, branch='main', gh_token=None):
    raw_link = str(get_configuration_github_path(sdk_id, branch))
    _LOGGER.debug('Will try to download: %s', raw_link)
    _LOGGER.debug('Token is defined: %s', gh_token is not None)
    headers = {'Authorization': 'token {}'.format(gh_token)} if gh_token else {}
    response = requests.get(raw_link, headers=headers)
    if response.status_code != 200:
        raise ValueError('Unable to download conf file for SDK {} branch {}: status code {}'.format(sdk_id, branch, response.status_code))
    return json.loads(response.text)