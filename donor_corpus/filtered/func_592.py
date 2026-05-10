def makeVoteContent(user):
    game = user.gameObject
    playerObject = user.playerObject
    notReady = False
    voteEntries = game.get_Vote_Entries(playerObject)
    return render_template('roundContentVote.html', notReady=notReady, voteEntries=voteEntries)