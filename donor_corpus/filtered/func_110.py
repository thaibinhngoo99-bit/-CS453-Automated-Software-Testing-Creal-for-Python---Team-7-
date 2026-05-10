def test_get_task_stream_save(client, tmpdir):
    bokeh = pytest.importorskip('bokeh')
    tmpdir = str(tmpdir)
    fn = os.path.join(tmpdir, 'foo.html')
    with get_task_stream(plot='save', filename=fn) as ts:
        wait(client.map(inc, range(10)))
    with open(fn) as f:
        data = f.read()
    assert 'inc' in data
    assert 'bokeh' in data
    assert isinstance(ts.figure, bokeh.plotting.Figure)