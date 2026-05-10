def generate(env):
    """Add Builders and construction variables for sunf77 to an Environment."""
    add_all_to_env(env)
    fcomp = env.Detect(compilers) or 'f77'
    env['FORTRAN'] = fcomp
    env['F77'] = fcomp
    env['SHFORTRAN'] = '$FORTRAN'
    env['SHF77'] = '$F77'
    env['SHFORTRANFLAGS'] = SCons.Util.CLVar('$FORTRANFLAGS -KPIC')
    env['SHF77FLAGS'] = SCons.Util.CLVar('$F77FLAGS -KPIC')