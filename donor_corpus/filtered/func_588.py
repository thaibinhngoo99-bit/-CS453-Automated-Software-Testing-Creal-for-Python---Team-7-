def revoking(certfile, serial):
    child = openssl('ca', '-revoke', certfile)
    ret = child.expect(['Already revoked', 'Revoking Certificate', pexpect.EOF])
    if ret == 0:
        msg = '[ERROR]: This certificate is revoked!'
        return jsonMessage(-1, msg)
    elif ret == 1:
        msg = 'Revoke Certificate success! Serial number is ' + serial
        gencrl()
        return jsonMessage(0, msg, {'Serial Number': serial})
    elif ret == 2:
        msg = '[ERROR]: Revoke failed, unknown error!'
        return jsonMessage(-1, msg)