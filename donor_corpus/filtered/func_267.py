@app.route('/tickets/close/<int:ticket_id>', methods=['POST'])
@requires_auth
def close_ticket(ticket_id):
    ticket_id = int(ticket_id)
    cursor = mysql.cursor()
    cursor.execute('UPDATE tickets SET done = 1 WHERE id = %s;', ticket_id)
    mysql.database.commit()
    return json.dumps({'result': 'success'})