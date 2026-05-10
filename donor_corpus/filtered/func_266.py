@app.route('/tickets/respond/<int:ticket_id>')
@requires_auth
def respond_to_ticket(ticket_id):
    response = request.form.get('response')
    cursor = mysql.cursor()
    cursor.execute('UPDATE tickets SET response = %s WHERE id = %s;', (response, ticket_id))
    mysql.database.commit()
    return jsonify({'result': 'success'})