@socketio.on('connected')
def client_connect():
    verbose = False or debugging
    '\n    I need to identify the user. If the user reloads, the session ID will change.\n    A unique user-key is provisided for each new user, and the session ID is updated\n    when the user reconnects. The unique ID is stored in a cookie.\n\n    '
    if verbose:
        print('Someone connected with the IP: {}'.format(request.remote_addr))
    uniqueID = request.cookies.get('uniqueID')
    if verbose:
        print('\nUnique ID before update: {}'.format(uniqueID))
    if uniqueID:
        if verbose:
            print('Unique ID cookie found')
        user = clients.find_User_By_uniqueID(uniqueID)
        if user:
            if verbose:
                print('User found')
            if request.sid != user.sid:
                user.sid = request.sid
                if verbose:
                    print('Updated the SID')
        else:
            user = clients.add_User(sid=request.sid)
            if verbose:
                print('User created')
            user.uniqueID = uniqueID
            if verbose:
                print('Unique ID updated')
    else:
        if verbose:
            print('Made a new user')
        user = clients.add_User(sid=request.sid)
        if verbose:
            print('Emitted to server: set_cookie')
        emit(arg=('set_cookie', {'name': 'uniqueID', 'data': user.uniqueID}), uniqueID=None, lock=timerLock, user=user)