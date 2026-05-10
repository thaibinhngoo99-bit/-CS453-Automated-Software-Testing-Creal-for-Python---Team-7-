@socketio.on('submit_supply')
def submitSupply(data):
    verbose = False or debugging
    if verbose:
        print('\n---------------------\nSupply reveived by the server')
    uniqueID = request.cookies.get('uniqueID')
    user = clients.find_User_By_uniqueID(uniqueID)
    if not user:
        if verbose:
            print('No user found when collecting the data')
        return
    game = user.gameObject
    if verbose:
        print('The data received is: {}'.format(data))
    if verbose:
        print('player {} found'.format(user.playerObject.name))
    if not data:
        return
    if verbose:
        print('')
    if verbose:
        print('The actual data:')
    for key, value in data.items():
        if verbose:
            print('Key: {} \t Value: {}'.format(key, value))
        if value == '':
            continue
        game.entries[int(key)].add_Autocomplete(value, user.playerObject)
    if verbose:
        print('')
    game.nrOfSupply += 1
    if verbose:
        print('The game has received {}nr of supplies\n---------------------\n'.format(game.nrOfSupply))
    if user.gameObject.nrOfSupply >= user.gameObject.get_Nr_Of_Players():
        if verbose:
            print('We should now refresh the div content')
        emitToGame(game=user.gameObject, arg=('refresh_div_content', {'div': 'contentVote', 'cont': '/gameRoomContent'}), lock=timerLock)
    if verbose and False:
        print('')
        for entry in game.entries:
            print('-------------------------------------------')
            print('The entry with the serch string: \t {}\nHas the following autocompletes added:'.format(entry.searchString))
            for supply in entry.otherAutocompletes:
                print(supply.autoComplete)
            print('-------------------------------------------')
        print('')