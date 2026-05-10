def build_swaggertosdk_conf_from_json_readme(readme_file, sdk_git_id, config, base_folder='.', force_generation=False):
    """Get the JSON conf of this README, and create SwaggerToSdk conf.

    Readme path can be any readme syntax accepted by autorest.
    readme_file will be project key as-is.

    :param str readme_file: A path that Autorest accepts. Raw GH link or absolute path.
    :param str sdk_dit_id: Repo ID. IF org/login is provided, will be stripped.
    :param dict config: Config where to update the "projects" key.
    :param bool force_generation: If no Swagger to SDK section is found, force once with the Readme as input
    """
    readme_full_path = get_readme_path(readme_file, base_folder)
    with tempfile.TemporaryDirectory() as temp_dir:
        readme_as_conf = autorest_swagger_to_sdk_conf(readme_full_path, temp_dir, config)
    generated_config = {'markdown': readme_full_path}
    sdk_git_short_id = sdk_git_id.split('/')[-1].lower()
    _LOGGER.info('Looking for tag {} in readme {}'.format(sdk_git_short_id, readme_file))
    for swagger_to_sdk_conf in readme_as_conf:
        if not isinstance(swagger_to_sdk_conf, dict):
            continue
        repo = swagger_to_sdk_conf.get('repo', '')
        repo = repo.split('/')[-1].lower()
        if repo == sdk_git_short_id:
            _LOGGER.info('This Readme contains a swagger-to-sdk section for repo {}'.format(repo))
            generated_config.update({'autorest_options': swagger_to_sdk_conf.get('autorest_options', {}), 'after_scripts': swagger_to_sdk_conf.get('after_scripts', [])})
            config.setdefault('projects', {})[str(readme_file)] = generated_config
            return generated_config
        else:
            _LOGGER.info('Skip mismatch {} from {}'.format(repo, sdk_git_short_id))
    if not force_generation:
        _LOGGER.info("Didn't find tag {} in readme {}. Did you forget to update the SwaggerToSdk section?".format(sdk_git_short_id, readme_file))
    else:
        _LOGGER.info("Didn't find tag {} in readme {}. Forcing it.".format(sdk_git_short_id, readme_file))
        config.setdefault('projects', {})[str(readme_file)] = generated_config