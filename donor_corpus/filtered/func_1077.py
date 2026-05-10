def make_symlinks(src_bin, symlink_dir, version):
    if not os.path.isfile(src_bin):
        raise ValueError(f"{src_bin} doesn't exist.")
    system = current_system()
    if symlink_dir not in map(os.path.normpath, os.environ['PATH'].split(os.pathsep)):
        print(f'add {symlink_dir} to PATH')
        if system == 'winnt':
            subprocess.run(['powershell.exe', 'setx', 'PATH', f'"$env:PATH;{symlink_dir}"'])
        else:
            msg = '~/.bashrc will be modified'
            msg += "\nif you're not using BASH, then you'll need manually"
            msg += f' add {symlink_dir} to your PATH'
            print(msg)
            rc_file = os.path.expanduser('~/.bashrc')
            with open(rc_file, 'a') as file:
                file.writelines('\n# added by jill\n')
                file.writelines(f'export PATH={symlink_dir}:$PATH\n')
        print(f'you need to restart your current shell to update PATH')
    os.makedirs(symlink_dir, exist_ok=True)
    new_ver = Version(get_exec_version(src_bin))
    if version == 'latest':
        link_list = ['julia-latest']
    elif len(Version(version).build) > 0:
        link_list = ['julia-dev']
    elif len(new_ver.prerelease) > 0:
        link_list = [f'julia-{f_minor_version(version)}']
    else:
        link_list = [f'julia-{f(version)}' for f in (f_major_version, f_minor_version)]
        link_list.append('julia')
    for linkname in link_list:
        linkpath = os.path.join(symlink_dir, linkname)
        if current_system() == 'winnt':
            linkpath += '.cmd'
        if os.path.exists(linkpath) or os.path.islink(linkpath):
            if os.path.islink(linkpath) and os.readlink(linkpath) == src_bin:
                continue
            old_ver = Version(get_exec_version(linkpath))
            if show_verbose():
                print(f'old symlink version: {old_ver}')
                print(f'new installation version: {new_ver}')
            if old_ver > new_ver:
                continue
            msg = f'{color.YELLOW}remove old symlink'
            msg += f' {linkname}{color.END}'
            print(msg)
            os.remove(linkpath)
        print(f'{color.GREEN}make new symlink {linkpath}{color.END}')
        if current_system() == 'winnt':
            with open(linkpath, 'w') as f:
                f.writelines(['@echo off\n', f'"{src_bin}" %*'])
        else:
            os.symlink(src_bin, linkpath)