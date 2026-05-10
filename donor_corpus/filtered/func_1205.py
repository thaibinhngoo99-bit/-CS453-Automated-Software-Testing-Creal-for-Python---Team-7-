@app.route('/screen/<int:sid>/clone', methods=['GET', 'POST'])
def dash_screen_clone(sid):
    screen = DashboardScreen.get(sid)
    if not screen:
        abort(404, 'no such screen')
    if request.method == 'POST':
        screen_name = request.form.get('screen_name')
        with_graph = request.form.get('with_graph')
        new_s = DashboardScreen.add(screen.pid, screen_name)
        if not new_s:
            abort(404, '创建screen失败了')
        if with_graph:
            old_graphs = DashboardGraph.gets_by_screen_id(sid)
            for o in old_graphs:
                DashboardGraph.add(o.title, o.hosts, o.counters, new_s.id, o.timespan, o.graph_type, o.method, o.position)
        return redirect('/screen/%s' % new_s.id)
    else:
        return render_template('screen/clone.html', **locals())