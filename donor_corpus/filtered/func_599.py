@socketio.on('submit_favorite')
def submitFavorite(favorite):
    print('The server received a favorite: {}'.format(favorite))
    uniqueID = request.cookies.get('uniqueID')
    user = clients.find_User_By_uniqueID(uniqueID)
    game = user.gameObject
    autoComplete = game.get_Autocomlete_by_ID(favorite)
    if not autoComplete:
        user.playerObject.points -= 1
        return
    user.playerObject.autocompleteVotedFor = autoComplete
    if autoComplete.isGoogle:
        user.playerObject.points += 1
        return
    autoComplete.playerObject.points += 1
    return