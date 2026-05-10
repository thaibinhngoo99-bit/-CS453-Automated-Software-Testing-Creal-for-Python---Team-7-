def revokeFromSerial(serial):
    path = os.path.join(CA_NEWCERTS, serial + '.pem')
    if not os.path.exists(path):
        msg = '[ERROR]: This may be an invalid serial number!'
        return jsonMessage(-1, msg)
    return revoking(path, serial)