@app.route('/screen/<int:sid>/edit', methods=['GET', 'POST'])
def dash_screen_edit(sid):
    screen = DashboardScreen.get(sid)
    if not screen:
        abort(404, 'no such screen')
    if request.method == 'POST':
        screen_name = request.form.get('screen_name')
        screen.update(name=screen_name)
        return redirect('/screen/%s' % screen.id)
    else:
        return render_template('screen/edit.html', **locals())