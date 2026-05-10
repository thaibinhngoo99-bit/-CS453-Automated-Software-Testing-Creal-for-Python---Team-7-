@app.route('/screen/<int:sid>')
def dash_screen(sid):
    start = request.args.get('start')
    end = request.args.get('end')
    top_screens = DashboardScreen.gets(pid=0)
    top_screens = sorted(top_screens, key=lambda x: x.name)
    screen = DashboardScreen.get(sid)
    if not screen:
        abort(404, 'no screen')
    if str(screen.pid) == '0':
        sub_screens = DashboardScreen.gets(pid=sid)
        sub_screens = sorted(sub_screens, key=lambda x: x.name)
        return render_template('screen/top_screen.html', **locals())
    pscreen = DashboardScreen.get(screen.pid)
    sub_screens = DashboardScreen.gets(pid=screen.pid)
    sub_screens = sorted(sub_screens, key=lambda x: x.name)
    graphs = DashboardGraph.gets_by_screen_id(screen.id)
    all_graphs = []
    for graph in graphs:
        all_graphs.extend(generate_graph_urls(graph, start, end) or [])
    all_graphs = sorted(all_graphs, key=lambda x: x.position)
    return render_template('screen/screen.html', **locals())