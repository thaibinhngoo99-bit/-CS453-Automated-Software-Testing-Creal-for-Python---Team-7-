@socketio.on('handle_chat')
def handleChat(msg):
    verbose = False or debugging
    uniqueID = request.cookies.get('uniqueID')
    user = clients.find_User_By_uniqueID(uniqueID)
    if not user:
        if verbose:
            print('No user')
        return redirect(url_for('index'))
    game = user.gameObject
    if not game:
        if verbose:
            print('No game found when handling chat')
        return
    game.add_Chat_Msg(chatMsg=msg, playerName=user.playerObject.name)
    emitToGame(game=game, arg=('update_chat', {}), lock=timerLock)