@app.route('/tickets/get/open')
@requires_auth
def get_open_tickets():
    cursor = mysql.cursor()
    cursor.execute('SELECT * FROM tickets WHERE done = 0;')
    return jsonify({'tickets': cursor.fetchall()})