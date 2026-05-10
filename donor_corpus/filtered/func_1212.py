def nicovideo_login(user, password):
    data = 'current_form=login&mail=' + user + '&password=' + password + '&login_submit=Log+In'
    response = request.urlopen(request.Request('https://secure.nicovideo.jp/secure/login?site=niconico', headers=fake_headers, data=data.encode('utf-8')))
    return response.headers