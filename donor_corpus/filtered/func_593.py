def makeRoundEnd(user):
    game = user.gameObject
    playerObject = user.playerObject
    playersPoints = {}
    for player in game.players:
        playersPoints[player.name] = player.points
    searchStrings = {}
    for entry in game.entries:
        searchStrings[entry.searchString] = {}
    return render_template('roundContentEnd.html', playersPoints=playersPoints)