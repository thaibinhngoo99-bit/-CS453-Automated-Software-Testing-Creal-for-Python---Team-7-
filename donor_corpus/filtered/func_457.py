def check_call(cmd_args, *args, **kwargs):
    cwd_str = '' if 'cwd' not in kwargs else f' (in cwd: {kwargs['cwd']})'
    _LOG.info('run%s: %s', cwd_str, ' '.join((shlex.quote(a) for a in cmd_args)))
    return subprocess.check_call(cmd_args, *args, **kwargs)