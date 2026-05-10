def run():
    username = random.choice(usernames)
    token = requests.get('http://' + siteurl + '/login/token.php?username=' + username + '&password=' + password + '&service=moodle_mobile_app').json()['token']
    print(f'{token}')