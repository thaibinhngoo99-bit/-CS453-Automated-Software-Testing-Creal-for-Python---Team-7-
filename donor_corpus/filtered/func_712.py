def ssh_execute(ssh, cmd, process_input=None, addl_env=None, check_exit_code=True):
    sanitized_cmd = strutils.mask_password(cmd)
    LOG.debug('Running cmd (SSH): %s', sanitized_cmd)
    if addl_env:
        raise InvalidArgumentError(_('Environment not supported over SSH'))
    if process_input:
        raise InvalidArgumentError(_('process_input not supported over SSH'))
    stdin_stream, stdout_stream, stderr_stream = ssh.exec_command(cmd)
    channel = stdout_stream.channel
    stdout = stdout_stream.read()
    sanitized_stdout = strutils.mask_password(stdout)
    stderr = stderr_stream.read()
    sanitized_stderr = strutils.mask_password(stderr)
    stdin_stream.close()
    exit_status = channel.recv_exit_status()
    if exit_status != -1:
        LOG.debug('Result was %s' % exit_status)
        if check_exit_code and exit_status != 0:
            raise ProcessExecutionError(exit_code=exit_status, stdout=sanitized_stdout, stderr=sanitized_stderr, cmd=sanitized_cmd)
    return (sanitized_stdout, sanitized_stderr)