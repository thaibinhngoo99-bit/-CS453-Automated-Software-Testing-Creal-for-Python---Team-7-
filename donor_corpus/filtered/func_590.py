@app.route('/gameRoom', methods=['POST', 'GET'])
def gameRoom():
    global games
    verbose = False or debugging
    argumentsMakeGame = ['name', 'gameName', 'nrOfRounds', 'time', 'newGame']
    argumentsJoinGame = ['name', 'gameName', 'newGame']
    uniqueID = request.cookies.get('uniqueID')
    user = clients.find_User_By_uniqueID(uniqueID)
    if not user:
        return redirect(url_for('index') + '?error=No user. Refreshing')
    if not user.gameObject:
        data = request.form
        if data['newGame'] == 'yes':
            if verbose:
                print('In server:gameRoom() nrOfRounds set!')
            for key in data.keys():
                argumentsMakeGame.remove(key)
            if argumentsMakeGame:
                return redirect(url_for('index') + '?error=Not enough arguments when creating the game')
            if verbose:
                print('In server:gameRoom() arguments needed for making a game are present')
            game = games.add_Game(gameName=data['gameName'], nrOfRounds=data['nrOfRounds'], timePerRound=data['time'])
            player = game.add_Player(name=data['name'], userObject=user)
            if not player:
                return redirect(url_for('index') + '?error=Player name already exists in this game...')
            if verbose:
                print('In server:gameRoom() game created with the name {} and user/player added'.format(game.gameName))
        else:
            data = request.form
            if verbose:
                print('In server:gameRoom() joining a game!')
            for key in data.keys():
                argumentsJoinGame.remove(key)
            if argumentsJoinGame:
                return redirect(url_for('index') + '?error=Not enough arguments when joining the game')
            if verbose:
                print('In server:gameRoom() Searching for game: {}'.format(data['gameName']))
            game = games.find_Game_By_Name(data['gameName'], verbose)
            if not game:
                if verbose:
                    print('The game was not found')
                return redirect(url_for('index') + '?error=Game not found')
            for player in game.players:
                if player.name == data['name']:
                    return redirect(url_for('index') + '?error=Name already taken')
            player = game.add_Player(name=data['name'], userObject=user)
            if verbose:
                print('In server:gameRoom() Player joined game')
            if verbose:
                print('In server:gameRoom() game created and user/player added')
            sendMessageToGame(game, '{} joined the game'.format(data['name']))
            emitToGame(game=game, arg=('refresh_Player_List', {}), lock=timerLock)
    elif verbose:
        print('User alreade in game')
    error = None
    return make_response(render_template('gameRoom.html', title='Game Room', gameName=user.gameObject.gameName, error=error))