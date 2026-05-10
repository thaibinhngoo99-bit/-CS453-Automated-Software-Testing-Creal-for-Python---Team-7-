@app.route('/tickets/get')
@app.route('/tickets/get/<int:team_id>')
@requires_auth
def get_all_tickets(team_id=None):
    cursor = mysql.cursor()
    if not team_id:
        cursor.execute('SELECT * FROM tickets')
    else:
        cursor.execute('SELECT * FROM tickets where team_id = %d;', team_id)
    tks = cursor.fetchall()
    for t in tks:
        t['msg'] = t['msg'].decode('utf-8')
        t['response'] = t['response'].decode('utf-8')
    return jsonify({'tickets': tks})