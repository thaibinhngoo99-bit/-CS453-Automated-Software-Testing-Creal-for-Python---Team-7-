@app.route('/screen', methods=['GET', 'POST'])
def dash_screens():
    top_screens = DashboardScreen.gets(pid='0')
    top_screens = sorted(top_screens, key=lambda x: x.name)
    return render_template('screen/index.html', **locals())