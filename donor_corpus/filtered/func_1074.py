def is_installed(version, check_symlinks=True):
    """
        check if the required version is already installed.
    """
    check_list = ['julia']
    if version == 'latest':
        check_list.append('julia-latest')
    if version != 'latest' and check_symlinks:
        check_list.extend([f'julia-{f_major_version(version)}', f'julia-{f_minor_version(version)}'])
    for path in check_list:
        if Version(get_exec_version(shutil.which(path))) != Version(version):
            return False
    return True