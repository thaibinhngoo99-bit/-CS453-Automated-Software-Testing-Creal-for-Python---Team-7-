@app.route('/screen/<int:sid>/graph', methods=['GET', 'POST'])
def dash_graph_add(sid):
    all_screens = DashboardScreen.gets()
    top_screens = [x for x in all_screens if x.pid == '0']
    children = []
    for t in top_screens:
        children.append([x for x in all_screens if x.pid == t.id])
    screen = DashboardScreen.get(sid)
    if not screen:
        abort(404, 'no screen')
    pscreen = DashboardScreen.get(screen.pid)
    if request.method == 'POST':
        title = request.form.get('title')
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
        graph = DashboardGraph.add(title, hosts, counters, sid, timespan, graph_type, method, position)
        return redirect('/screen/%s' % sid)
    else:
        gid = request.args.get('gid')
        graph = gid and DashboardGraph.get(gid)
        return render_template('screen/graph_add.html', config=config, **locals())