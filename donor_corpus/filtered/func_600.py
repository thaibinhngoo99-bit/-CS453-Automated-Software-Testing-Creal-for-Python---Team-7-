@socketio.on('toggle_ready')
def toggleReady(msg):
    verbose = True or debugging
    uniqueID = request.cookies.get('uniqueID')
    user = clients.find_User_By_uniqueID(uniqueID)
    if not user:
        if verbose:
            print('No user found when toggling ready')
        return
    player = user.playerObject
    if not player:
        if verbose:
            print('No player found for the user/client.')
    player.ready = not player.ready
    game = player.gameObject
    emitToGame(game=game, arg=('refresh_Player_List', {}), lock=timerLock)
    playersReady = game.all_Players_Ready()
    if verbose:
        print('STAGE:', game.get_Stage())
    if playersReady and game.gameStarted == False and (not game.spawnedThread):
        game.gameStarted = True
        game.reset_Players_Ready()
        emitToGame(game=game, arg=('change_content', {'url': '/gameRoomContent'}), lock=timerLock)
        emitToGame(game=game, arg=('client_message', {'msg': 'Game started. Have fun!'}), lock=timerLock)
        game.spawnedThread = RoundTimer(int(game.timePerRound), user)
        game.spawnedThread.start()
        return
    if playersReady and game.get_Stage() == 'roundStart':
        if verbose:
            print('Round ended by users')
        user.gameObject.end_Stage()
        game.reset_Players_Ready()
        if verbose:
            print('Current stage of game is: {}'.format(user.gameObject.get_Stage()))
        emitToGame(game=user.gameObject, arg=('round_End', {}), lock=timerLock)
        emitToGame(game=user.gameObject, arg=('client_message', {'msg': 'Round ended'}), lock=timerLock)
        return
    if playersReady and game.get_Stage() == 'roundSupply':
        user.gameObject.end_Stage()
        game.reset_Players_Ready()
        emitToGame(game=user.gameObject, arg=('supply_End', {'nrOfEntries': user.gameObject.nrOfEntry}), lock=timerLock)
        emitToGame(game=user.gameObject, arg=('client_message', {'msg': 'Round ended'}), lock=timerLock)
        return
    if playersReady and game.get_Stage() == 'roundVote':
        user.gameObject.end_Stage()
        game.reset_Players_Ready()
        emitToGame(game=user.gameObject, arg=('vote_End', {}), lock=timerLock)
        emitToGame(game=user.gameObject, arg=('client_message', {'msg': 'Vote ended'}), lock=timerLock)
        return