@app.route('/screen/embed/<int:sid>')
def dash_screen_embed(sid):
    start = request.args.get('start')
    end = request.args.get('end')
    screen = DashboardScreen.get(sid)
    if not screen:
        abort(404, 'no screen')
    if screen.pid == '0':
        abort(404, 'top screen')
    graphs = DashboardGraph.gets_by_screen_id(screen.id)
    all_graphs = []
    for graph in graphs:
        all_graphs.extend(generate_graph_urls(graph, start, end) or [])
    all_graphs = sorted(all_graphs, key=lambda x: x.position)
    return render_template('screen/screen_embed.html', **locals())