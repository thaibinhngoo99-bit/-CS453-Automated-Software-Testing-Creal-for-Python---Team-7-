def execute(*cmd, **kwargs):
    """Helper method to shell out and execute a command through subprocess.

    Allows optional retry.

    :param cmd:             Passed to subprocess.Popen.
    :type cmd:              string
    :param process_input:   Send to opened process.
    :type process_input:    string
    :param env_variables:   Environment variables and their values that
                            will be set for the process.
    :type env_variables:    dict
    :param check_exit_code: Single bool, int, or list of allowed exit
                            codes.  Defaults to [0].  Raise
                            :class:`ProcessExecutionError` unless
                            program exits with one of these code.
    :type check_exit_code:  boolean, int, or [int]
    :param delay_on_retry:  True | False. Defaults to True. If set to True,
                            wait a short amount of time before retrying.
    :type delay_on_retry:   boolean
    :param attempts:        How many times to retry cmd.
    :type attempts:         int
    :param run_as_root:     True | False. Defaults to False. If set to True,
                            the command is prefixed by the command specified
                            in the root_helper kwarg.
    :type run_as_root:      boolean
    :param root_helper:     command to prefix to commands called with
                            run_as_root=True
    :type root_helper:      string
    :param shell:           whether or not there should be a shell used to
                            execute this command. Defaults to false.
    :type shell:            boolean
    :param loglevel:        log level for execute commands.
    :type loglevel:         int.  (Should be logging.DEBUG or logging.INFO)
    :returns:               (stdout, stderr) from process execution
    :raises:                :class:`UnknownArgumentError` on
                            receiving unknown arguments
    :raises:                :class:`ProcessExecutionError`
    """
    process_input = kwargs.pop('process_input', None)
    env_variables = kwargs.pop('env_variables', None)
    check_exit_code = kwargs.pop('check_exit_code', [0])
    ignore_exit_code = False
    delay_on_retry = kwargs.pop('delay_on_retry', True)
    attempts = kwargs.pop('attempts', 1)
    run_as_root = kwargs.pop('run_as_root', False)
    root_helper = kwargs.pop('root_helper', '')
    shell = kwargs.pop('shell', False)
    loglevel = kwargs.pop('loglevel', logging.DEBUG)
    if isinstance(check_exit_code, bool):
        ignore_exit_code = not check_exit_code
        check_exit_code = [0]
    elif isinstance(check_exit_code, int):
        check_exit_code = [check_exit_code]
    if kwargs:
        raise UnknownArgumentError(_('Got unknown keyword args: %r') % kwargs)
    if run_as_root and hasattr(os, 'geteuid') and (os.geteuid() != 0):
        if not root_helper:
            raise NoRootWrapSpecified(message=_('Command requested root, but did not specify a root helper.'))
        cmd = shlex.split(root_helper) + list(cmd)
    cmd = map(str, cmd)
    sanitized_cmd = strutils.mask_password(' '.join(cmd))
    while attempts > 0:
        attempts -= 1
        try:
            LOG.log(loglevel, _('Running cmd (subprocess): %s'), sanitized_cmd)
            _PIPE = subprocess.PIPE
            if os.name == 'nt':
                preexec_fn = None
                close_fds = False
            else:
                preexec_fn = _subprocess_setup
                close_fds = True
            obj = subprocess.Popen(cmd, stdin=_PIPE, stdout=_PIPE, stderr=_PIPE, close_fds=close_fds, preexec_fn=preexec_fn, shell=shell, env=env_variables)
            result = None
            for _i in six.moves.range(20):
                try:
                    if process_input is not None:
                        result = obj.communicate(process_input)
                    else:
                        result = obj.communicate()
                except OSError as e:
                    if e.errno in (errno.EAGAIN, errno.EINTR):
                        continue
                    raise
                break
            obj.stdin.close()
            _returncode = obj.returncode
            LOG.log(loglevel, 'Result was %s' % _returncode)
            if not ignore_exit_code and _returncode not in check_exit_code:
                stdout, stderr = result
                sanitized_stdout = strutils.mask_password(stdout)
                sanitized_stderr = strutils.mask_password(stderr)
                raise ProcessExecutionError(exit_code=_returncode, stdout=sanitized_stdout, stderr=sanitized_stderr, cmd=sanitized_cmd)
            return result
        except ProcessExecutionError:
            if not attempts:
                raise
            else:
                LOG.log(loglevel, _('%r failed. Retrying.'), sanitized_cmd)
                if delay_on_retry:
                    greenthread.sleep(random.randint(20, 200) / 100.0)
        finally:
            greenthread.sleep(0)