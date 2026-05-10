def install_julia(version=None, *, install_dir=None, symlink_dir=None, upgrade=False, upstream=None, unstable=False, keep_downloads=False, confirm=False, reinstall=False):
    """
    Install the Julia programming language for your current system

    `jill install [version]` would satisfy most of your use cases, try it first
    and then read description of other arguments. `version` is optional, valid
    version syntax for it is:

    * `stable`: latest stable Julia release. This is the _default_ option.
    * `1`: latest `1.y.z` Julia release.
    * `1.0`: latest `1.0.z` Julia release.
    * `1.4.0-rc1`: as it is.
    * `latest`/`nightly`: the nightly builds from source code.

    For Linux/FreeBSD systems, if you run this command with `root` account,
    then it will install Julia system-widely.

    To download from a private mirror, please check `jill download -h`.

    Arguments:
      version:
        The Julia version you want to install.
      upstream:
        manually choose a download upstream. For example, set it to "Official"
        if you want to download from JuliaComputing's s3 buckets.
      upgrade:
        add `--upgrade` flag also copy the root environment from an older
        Julia version.
      unstable:
        add `--unstable` flag to allow installation of unstable releases for auto version
        query. For example, `jill install --unstable` might give you unstable installation
        like `1.7.0-beta1`. Note that if you explicitly pass the unstable version, e.g.,
        `jill install 1.7.0-beta1`, it will still work.
      keep_downloads:
        add `--keep_downloads` flag to not remove downloaded releases.
      confirm: add `--confirm` flag to skip interactive prompt.
      reinstall:
        jill will skip the installation if the required Julia version already exists,
        add `--reinstall` flag to force the reinstallation.
      install_dir:
        where you want julia packages installed.
      symlink_dir:
        where you want symlinks(e.g., `julia`, `julia-1`) placed.
    """
    install_dir = install_dir if install_dir else default_install_dir()
    install_dir = os.path.abspath(install_dir)
    symlink_dir = symlink_dir if symlink_dir else default_symlink_dir()
    symlink_dir = os.path.normpath(os.path.abspath(symlink_dir))
    system, arch = (current_system(), current_architecture())
    version = str(version) if version or str(version) == '0' else ''
    version = 'latest' if version == 'nightly' else version
    version = '' if version == 'stable' else version
    upstream = upstream if upstream else os.environ.get('JILL_UPSTREAM', None)
    if system == 'linux' and current_libc() == 'musl':
        system = 'musl'
    hello_msg()
    if system == 'winnt':
        install_dir = install_dir.replace('\\\\', '\\').strip('\'"')
    if not confirm:
        version_str = version if version else 'latest stable release'
        question = 'jill will:\n'
        question += f'  1) install Julia {version_str} for {system}-{arch}'
        question += f' into {color.UNDERLINE}{install_dir}{color.END}\n'
        question += f'  2) make symlinks in {color.UNDERLINE}{symlink_dir}{color.END}\n'
        question += f'You may need to manually add {color.UNDERLINE}{symlink_dir}{color.END} to PATH\n'
        question += 'Continue installation?'
        to_continue = query_yes_no(question)
        if not to_continue:
            return False
    if upstream:
        verify_upstream(upstream)
    wrong_args = False
    try:
        version = latest_version(version, system, arch, upstream=upstream, stable_only=not unstable)
    except ValueError:
        wrong_args = True
    if wrong_args:
        msg = f'wrong version(>= 0.6.0) argument: {version}\n'
        msg += f'Example: `jill install 1`'
        raise ValueError(msg)
    if not reinstall and is_installed(version):
        print(f'julia {version} already installed.')
        return True
    overwrite = True if version == 'latest' else False
    print(f'{color.BOLD}----- Download Julia -----{color.END}')
    package_path = download_package(version, system, arch, upstream=upstream, overwrite=overwrite)
    if not package_path:
        return False
    if package_path.endswith('.dmg'):
        installer = install_julia_dmg
    elif package_path.endswith('.tar.gz'):
        installer = install_julia_tarball
    elif package_path.endswith('.exe'):
        installer = install_julia_exe
    else:
        print(f'{color.RED}Unsupported file format for {package_path}{color.END}.')
    print(f'{color.BOLD}----- Install Julia -----{color.END}')
    installer(package_path, install_dir, symlink_dir, version, upgrade)
    if not keep_downloads:
        print(f'{color.BOLD}----- Post Installation -----{color.END}')
        print('remove downloaded files...')
        print(f'remove {package_path}')
        os.remove(package_path)
        gpg_signature_file = package_path + '.asc'
        if os.path.exists(gpg_signature_file):
            print(f'remove {gpg_signature_file}')
            os.remove(gpg_signature_file)
    print(f'{color.GREEN}Done!{color.END}')