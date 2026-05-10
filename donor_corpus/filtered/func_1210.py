@app.route('/graph/<int:gid>/edit', methods=['GET', 'POST'])
def dash_graph_edit(gid):
    error = ''
    graph = DashboardGraph.get(gid)
    if not graph:
        abort(404, 'no graph')
    all_screens = DashboardScreen.gets()
    top_screens = [x for x in all_screens if x.pid == '0']
    children = []
    for t in top_screens:
        children.append([x for x in all_screens if x.pid == t.id])
    screen = DashboardScreen.get(graph.screen_id)
    if not screen:
        abort(404, 'no screen')
    pscreen = DashboardScreen.get(screen.pid)
    if request.method == 'POST':
        ajax = request.form.get('ajax', '')
        screen_id = request.form.get('screen_id')
        title = request.form.get('title', '').strip()
        hosts = request.form.get('hosts', '').strip()
        hosts = hosts and hosts.split('\n') or []
        hosts = [x.strip() for x in hosts]
        counters = request.form.get('counters', '').strip()
        counters = counters and counters.split('\n') or []
        counters = [x.strip() for x in counters]
        timespan = request.form.get('timespan', 3600)
        graph_type = request.form.get('graph_type', 'h')
        method = request.form.get('method', '').upper()
        position = request.form.get('position', 0)
        graph = graph.update(title, hosts, counters, screen_id, timespan, graph_type, method, position)
        error = u'修改成功了'
        if not ajax:
            return render_template('screen/graph_edit.html', config=config, **locals())
        else:
            return 'ok'
    else:
        ajax = request.args.get('ajax', '')
        return render_template('screen/graph_edit.html', **locals())