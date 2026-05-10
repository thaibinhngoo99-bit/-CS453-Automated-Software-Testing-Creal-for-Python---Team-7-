def save(name, file):
    encoded_name = str(base64.urlsafe_b64encode(name.encode('utf-8')), 'utf-8')
    b = base.get(encoded_name)
    try:
        if b:
            base.put({'key': encoded_name, 'name': name, 'public': b['public'], 'lastModified': datetime.utcnow().timestamp()})
            return drive.put(name, file)
        base.put({'key': encoded_name, 'name': name, 'public': False, 'lastModified': datetime.utcnow().timestamp()})
        return drive.put(name, file)
    except:
        return None