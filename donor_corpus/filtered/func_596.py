@app.route('/leave_Game')
def leaveGame():
    verbose = False or debugging
    uniqueID = request.cookies.get('uniqueID')
    user = clients.find_User_By_uniqueID(uniqueID)
    if not user:
        if verbose:
            print('No user')
        return redirect(url_for('index'))
    game = user.gameObject
    game.remove_Player_By_User_Object(user)
    name = user.playerObject.name
    user.resetUser()
    if len(game.players) < 1:
        games.removeGame(game=game, verbose=verbose)
    else:
        emitToGame(game=game, arg=('refresh_Player_List', {}), lock=timerLock)
        emitToGame(game=game, arg=('client_warning', {'msg': name + ' left the game'}), lock=timerLock)
    print(len(games._games))
    return redirect(url_for('index'))