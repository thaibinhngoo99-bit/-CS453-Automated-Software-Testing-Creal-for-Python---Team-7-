def login(username, orgname=None, scope=None):
    iat = datetime.utcnow()
    exp = iat + timedelta(seconds=6000)
    payload = {'iss': 'acme.local', 'sub': username, 'iat': iat, 'exp': exp}
    if orgname:
        payload.update({'aud': orgname, 'scp': {'org': ['manage']}})
    if scope:
        payload.update({'scp': scope})
    token = jwt.encode(payload, 'secret').decode()
    return f'JWT {token}'