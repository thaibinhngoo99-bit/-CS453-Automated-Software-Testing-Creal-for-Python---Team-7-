def emit(arg, uniqueID, lock, user=None):
    """
    An emit method that requires a lock. Dunno if I need this...
    TODO: Find out if i need the lock.
    """
    verbose = False or debugging
    with lock:
        if verbose:
            print('Did an emit')
        if not user:
            userSID = clients.find_User_By_uniqueID(uniqueID).sid
        else:
            userSID = user.sid
        socketio.emit(*arg, room=userSID)