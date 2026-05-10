def get_drawing(name):
    encoded_name = str(base64.urlsafe_b64encode(name.encode('utf-8')), 'utf-8')
    b = base.get(encoded_name)
    d = drive.get(name)
    if b and d:
        return d.read()
    base.delete(encoded_name)
    drive.delete(name)
    return None