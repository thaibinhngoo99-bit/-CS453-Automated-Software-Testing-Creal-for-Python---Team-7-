def copy_root_project(version):
    mver = f_minor_version(version)
    old_ver = last_julia_version(version)
    if old_ver is None:
        print(f"Can't find available old root project for version {version}")
        return None
    env_path = os.path.join(default_depot_path(), 'environments')
    src_path = os.path.join(env_path, old_ver)
    dest_path = os.path.join(env_path, f'v{mver}')
    if src_path == dest_path:
        return None
    if os.path.exists(dest_path):
        bak_path = os.path.join(env_path, f'v{mver}.bak')
        if os.path.exists(bak_path):
            print(f'{color.YELLOW}delete old backup {bak_path}{color.END}')
            shutil.rmtree(bak_path)
        shutil.move(dest_path, bak_path)
        print(f'{color.YELLOW}move {dest_path} to {bak_path}{color.END}')
    shutil.copytree(src_path, dest_path)