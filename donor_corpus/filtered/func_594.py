@app.route('/playerList')
def playerList():
    uniqueID = request.cookies.get('uniqueID')
    user = clients.find_User_By_uniqueID(uniqueID)
    verbose = False or debugging
    if userNotComplete(user, verbose=False or debugging):
        return redirect(url_for('index') + '?error=User not in game')
    playerList = user.gameObject.get_Player_Names_And_Status()
    if verbose:
        print('Got {} players'.format(len(playerList)))
    return render_template('playerList.html', playerList=playerList)