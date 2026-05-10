def get_python_relative_libdir():
    """Returns the appropropriate python libdir relative to the build directory.

    @param exe_path the path to the lldb executable

    @return the python path that needs to be added to sys.path (PYTHONPATH)
    in order to find the lldb python module.
    """
    if platform.system() != 'Linux':
        return None
    arch_specific_libdir = distutils.sysconfig.get_python_lib(True, False)
    split_libdir = arch_specific_libdir.split(os.sep)
    lib_re = re.compile('^lib.+$')
    for i in range(len(split_libdir)):
        match = lib_re.match(split_libdir[i])
        if match is not None:
            return os.sep.join(split_libdir[i:])
    return None