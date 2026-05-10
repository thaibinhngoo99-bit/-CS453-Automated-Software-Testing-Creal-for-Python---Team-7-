@app.callback(Output('page-content', 'children'), Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return index.layout
    if pathname == '/record':
        return record.layout
    if pathname == '/watch':
        return watch.layout
    if pathname == '/replay':
        return replay.layout
    if pathname == '/about':
        return about.layout