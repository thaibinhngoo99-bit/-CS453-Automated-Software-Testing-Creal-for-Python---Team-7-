def revokeFromCert(cert):
    try:
        x509_obj = crypto.load_certificate(crypto.FILETYPE_PEM, cert)
        serial = hex(x509_obj.get_serial_number())[2:]
    except crypto.Error:
        return jsonMessage(status=-1, msg='[ERROR]: Wrong certificate (X509) format!')
    path = os.path.join('/tmp', hashlib.md5(str(datetime.datetime.now()).encode('utf-8')).hexdigest() + '_revokecert.crt')
    with open(path, 'w') as f:
        f.write(cert.decode('utf8'))
    return revoking(path, serial)