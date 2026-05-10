@synchronized(lock=SSL_CERT_LOCK)
def generate_ssl_cert(target_file=None, overwrite=False, random=False, return_content=False, serial_number=None):
    from OpenSSL import crypto

    def all_exist(*files):
        return all([os.path.exists(f) for f in files])
    if target_file and (not overwrite) and os.path.exists(target_file):
        key_file_name = '%s.key' % target_file
        cert_file_name = '%s.crt' % target_file
        if all_exist(key_file_name, cert_file_name):
            return (target_file, cert_file_name, key_file_name)
    if random and target_file:
        if '.' in target_file:
            target_file = target_file.replace('.', '.%s.' % short_uid(), 1)
        else:
            target_file = '%s.%s' % (target_file, short_uid())
    k = crypto.PKey()
    k.generate_key(crypto.TYPE_RSA, 2048)
    cert = crypto.X509()
    subj = cert.get_subject()
    subj.C = 'AU'
    subj.ST = 'Some-State'
    subj.L = 'Some-Locality'
    subj.O = 'LocalStack Org'
    subj.OU = 'Testing'
    subj.CN = 'localhost'
    serial_number = serial_number or 1001
    cert.set_version(2)
    cert.set_serial_number(serial_number)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(2 * 365 * 24 * 60 * 60)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(k)
    alt_names = b'DNS:localhost,DNS:test.localhost.atlassian.io,IP:127.0.0.1'
    cert.add_extensions([crypto.X509Extension(b'subjectAltName', False, alt_names), crypto.X509Extension(b'basicConstraints', True, b'CA:false'), crypto.X509Extension(b'keyUsage', True, b'nonRepudiation,digitalSignature,keyEncipherment'), crypto.X509Extension(b'extendedKeyUsage', True, b'serverAuth')])
    cert.sign(k, 'SHA256')
    cert_file = StringIO()
    key_file = StringIO()
    cert_file.write(to_str(crypto.dump_certificate(crypto.FILETYPE_PEM, cert)))
    key_file.write(to_str(crypto.dump_privatekey(crypto.FILETYPE_PEM, k)))
    cert_file_content = cert_file.getvalue().strip()
    key_file_content = key_file.getvalue().strip()
    file_content = '%s\n%s' % (key_file_content, cert_file_content)
    if target_file:
        key_file_name = '%s.key' % target_file
        cert_file_name = '%s.crt' % target_file
        if not all_exist(target_file, key_file_name, cert_file_name):
            for i in range(2):
                try:
                    save_file(target_file, file_content)
                    save_file(key_file_name, key_file_content)
                    save_file(cert_file_name, cert_file_content)
                    break
                except Exception as e:
                    if i > 0:
                        raise
                    LOG.info('Unable to store certificate file under %s, using tmp file instead: %s' % (target_file, e))
                    target_file = '%s.pem' % new_tmp_file()
                    key_file_name = '%s.key' % target_file
                    cert_file_name = '%s.crt' % target_file
            TMP_FILES.append(target_file)
            TMP_FILES.append(key_file_name)
            TMP_FILES.append(cert_file_name)
        if not return_content:
            return (target_file, cert_file_name, key_file_name)
    return file_content