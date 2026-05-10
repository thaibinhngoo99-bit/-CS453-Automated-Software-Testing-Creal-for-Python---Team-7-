@requires_auth
@app.route('/tickets/add', methods=['POST'])
def submit_ticket():
    team_id = request.form.get('team_id')
    subject = request.form.get('subject')
    msg = request.form.get('message')
    ts = request.form.get('ts')
    cursor = mysql.cursor()
    cursor.execute('INSERT INTO tickets\n                          (team_id, ts, subject, msg, response)\n                      VALUES (%s, %s, %s, %s, %s)', (team_id, ts, subject, msg, 'No Response Yet'))
    ticket_id = cursor.lastrowid
    mysql.database.commit()
    if cursor.rowcount == 0:
        return json.dumps({'result': 'fail'})
    else:
        return json.dumps({'result': 'success', 'ticket_id': ticket_id})