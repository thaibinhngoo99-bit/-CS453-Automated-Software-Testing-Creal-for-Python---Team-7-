def get_arch():
    if is_mac_os():
        return 'osx'
    if is_alpine():
        return 'alpine'
    if is_linux():
        return 'linux'
    raise Exception('Unable to determine system architecture')