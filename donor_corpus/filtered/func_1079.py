def install_julia_tarball(package_path, install_dir, symlink_dir, version, upgrade):
    check_installer(package_path, '.tar.gz')
    if re.match('(.*)\\+(\\w+)$', version):
        suffix = 'dev'
    else:
        suffix = f_minor_version(version)
    with TarMounter(package_path) as root:
        src_path = root
        dest_path = os.path.join(install_dir, f'julia-{suffix}')
        if os.path.exists(dest_path):
            shutil.rmtree(dest_path)
            msg = f'{color.YELLOW}remove previous Julia installation:'
            msg += f' {dest_path}{color.END}'
            print(msg)
        shutil.copytree(src_path, dest_path, symlinks=True)
        print(f'{color.GREEN}install Julia to {dest_path}{color.END}')
    os.chmod(dest_path, 493)
    bin_path = os.path.join(dest_path, 'bin', 'julia')
    if current_system() == 'winnt':
        bin_path += '.exe'
    make_symlinks(bin_path, symlink_dir, version)
    if upgrade:
        copy_root_project(version)
    return True