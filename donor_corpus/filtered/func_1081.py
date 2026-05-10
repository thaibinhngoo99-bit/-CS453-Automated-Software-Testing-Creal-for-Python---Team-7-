def install_julia_exe(package_path, install_dir, symlink_dir, version, upgrade):
    check_installer(package_path, '.exe')
    dest_path = os.path.join(install_dir, f'julia-{f_minor_version(version)}')
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path, ignore_errors=True)
        msg = f'{color.YELLOW}remove previous Julia installation:'
        msg += f' {dest_path}{color.END}'
        print(msg)
    if Version(version).next_patch() < Version('1.4.0'):
        subprocess.check_output([f'{package_path}', '/S', f'/D={dest_path}'])
    else:
        subprocess.check_output([f'{package_path}', '/VERYSILENT', f'/DIR={dest_path}'])
    print(f'{color.GREEN}install Julia to {dest_path}{color.END}')
    bin_path = os.path.join(dest_path, 'bin', 'julia.exe')
    make_symlinks(bin_path, symlink_dir, version)
    if upgrade:
        copy_root_project(version)
    return True