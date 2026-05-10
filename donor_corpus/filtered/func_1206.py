@app.route('/graph/<int:gid>/delete')
def dash_graph_delete(gid):
    graph = DashboardGraph.get(gid)
    if not graph:
        abort(404, 'no such graph')
    DashboardGraph.remove(gid)
    return redirect('/screen/' + graph.screen_id)