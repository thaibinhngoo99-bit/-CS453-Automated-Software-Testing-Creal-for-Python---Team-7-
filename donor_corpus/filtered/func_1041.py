def read_config(sdk_git_folder, config_file):
    """Read the configuration file and return JSON"""
    config_path = os.path.join(sdk_git_folder, config_file)
    with open(config_path, 'r') as config_fd:
        return json.loads(config_fd.read())