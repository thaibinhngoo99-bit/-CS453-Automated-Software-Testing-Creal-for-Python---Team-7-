def install_julia_dmg(package_path, install_dir, symlink_dir, version, upgrade):
    check_installer(package_path, '.dmg')
    with DmgMounter(package_path) as root:
        appname = next(filter(lambda x: x.lower().startswith('julia'), os.listdir(root)))
        src_path = os.path.join(root, appname)
        dest_path = os.path.join(install_dir, appname)
        if os.path.exists(dest_path):
            msg = f'{color.YELLOW}remove previous Julia installation:'
            msg += f' {dest_path}{color.END}'
            print(msg)
            shutil.rmtree(dest_path)
        shutil.copytree(src_path, dest_path, symlinks=True)
        print(f'{color.GREEN}install Julia to {dest_path}{color.END}')
    bin_path = os.path.join(dest_path, 'Contents', 'Resources', 'julia', 'bin', 'julia')
    make_symlinks(bin_path, symlink_dir, version)
    if upgrade:
        copy_root_project(version)
    return True