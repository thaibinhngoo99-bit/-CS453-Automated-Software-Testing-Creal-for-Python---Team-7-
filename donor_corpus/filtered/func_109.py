@gen_cluster(client=True)
async def test_get_task_stream_plot(c, s, a, b):
    bokeh = pytest.importorskip('bokeh')
    await c.get_task_stream()
    futures = c.map(slowinc, range(10), delay=0.1)
    await wait(futures)
    data, figure = await c.get_task_stream(plot=True)
    assert isinstance(figure, bokeh.plotting.Figure)