@socketio.on('submit_entry')
def submitEntry(msg):
    verbose = False or debugging
    if verbose:
        print('Entry reveived by the server')
    uniqueID = request.cookies.get('uniqueID')
    user = clients.find_User_By_uniqueID(uniqueID)
    if verbose:
        print('User retrieved')
    if not user:
        if verbose:
            print('No user found when collecting the data')
        return
    if user.playerObject.entry:
        if verbose:
            print('User already submitted.')
        return
    if verbose:
        print('Setting entry for user')
    user.gameObject.add_Entry(msg['searchString'], msg['suggestion'], user.playerObject)
    if verbose:
        print('Got entry')
    if user.gameObject.nrOfEntry >= user.gameObject.get_Nr_Of_Players():
        emitToGame(game=user.gameObject, arg=('refresh_div_content', {'div': 'entryList', 'cont': '/gameRoomContent'}), lock=timerLock)