@app.route('/chatContent')
def chatContent():
    uniqueID = request.cookies.get('uniqueID')
    user = clients.find_User_By_uniqueID(uniqueID)
    if userNotComplete(user, verbose=False or debugging):
        return redirect(url_for('index') + '?error=User not in game')
    chat = user.gameObject.chatMessages
    msgs = []
    players = []
    for msg in chat:
        player, msg = msg.get_Player_And_Msg()
        msgs.append(str(msg))
        players.append(str(player))
    if players:
        players.reverse()
        msgs.reverse()
    return render_template('chat.html', players=players, chatMsg=msgs)