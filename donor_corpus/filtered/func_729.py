def sftp_delete_remote_file(f):
    host = 'mpd.shack'
    port = 22
    transport = paramiko.Transport((host, port))
    username = 'shack'
    passwd = 'shackit'
    transport.connect(username=username, password=passwd)
    sftp = paramiko.SFTPClient.from_transport(transport)
    print(sftp.unlink('%s/%s' % (sftp_base_path, f)))
    sftp.close()
    transport.close()