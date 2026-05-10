def _find_conda():
    """Find the conda executable robustly across conda versions.

    Returns
    -------
    conda : str
        Path to the conda executable.

    Raises
    ------
    IOError
        If the executable cannot be found in either the CONDA_EXE environment
        variable or in the PATH.

    Notes
    -----
    In POSIX platforms in conda >= 4.4, conda can be set up as a bash function
    rather than an executable. (This is to enable the syntax
    ``conda activate env-name``.) In this case, the environment variable
    ``CONDA_EXE`` contains the path to the conda executable. In other cases,
    we use standard search for the appropriate name in the PATH.

    See https://github.com/airspeed-velocity/asv/issues/645 for more details.
    """
    if 'CONDA_EXE' in os.environ:
        conda = os.environ['CONDA_EXE']
    else:
        conda = util.which('conda')
    return conda