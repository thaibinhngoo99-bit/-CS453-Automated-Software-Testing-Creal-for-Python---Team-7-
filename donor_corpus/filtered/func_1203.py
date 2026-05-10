@app.route('/screen/<int:sid>/delete')
def dash_screen_delete(sid):
    screen = DashboardScreen.get(sid)
    if not screen:
        abort(404, 'no such screen')
    DashboardScreen.remove(sid)
    return redirect('/screen')