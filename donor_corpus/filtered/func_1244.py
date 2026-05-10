def save_as(name, file, overwrite):
    encoded_name = str(base64.urlsafe_b64encode(name.encode('utf-8')), 'utf-8')
    b = base.get(encoded_name)
    record = {'key': encoded_name, 'name': name, 'public': False, 'lastModified': datetime.utcnow().timestamp()}
    if overwrite or not b:
        base.put(record)
        drive.put(name, file)
        return record
    else:
        return None