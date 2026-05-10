@app.route('/gameRoomContent')
def gameRoomContent():
    uniqueID = request.cookies.get('uniqueID')
    user = clients.find_User_By_uniqueID(uniqueID)
    if userNotComplete(user, verbose=False or debugging):
        return 'ERROR: Something strange happened. Please leave game and rejoin'
    game = user.gameObject
    nrOfRounds = game.nrOfRounds
    timePerRound = game.timePerRound
    gameName = game.gameName
    roundNr = game.currentRound
    if user.gameObject.get_Stage() == 'lobby':
        return render_template('lobbyContent.html', gameName=gameName, nrOfRounds=nrOfRounds, timePerRound=timePerRound)
    elif user.gameObject.get_Stage() == 'roundStart':
        return render_template('roundContentStart.html', timePerRound=timePerRound, roundNr=roundNr, nrOfRounds=nrOfRounds)
    elif user.gameObject.get_Stage() == 'roundSupply':
        game.spawnedThread = None
        game.reset_Players_Ready()
        emitToGame(game=game, arg=('refresh_Player_List', {}), lock=timerLock)
        print('GameContent:')
        print(game.get_Search_Strings(user.playerObject))
        return render_template('roundContentSupply.html', nrOfPlayers=game.get_Nr_Of_Players(), searchStrings=game.get_Search_Strings(user.playerObject), nrOfEntries=game.nrOfEntry)
    elif user.gameObject.get_Stage() == 'roundVote':
        game.reset_Players_Ready()
        return makeVoteContent(user)
    elif user.gameObject.get_Stage() == 'roundEnd':
        game.reset_Players_Ready()
        return makeRoundEnd(user)
    elif user.gameObject.get_Stage() == 'gameSummary':
        game.reset_Players_Ready()
        return render_template('gameContentSummary.html')