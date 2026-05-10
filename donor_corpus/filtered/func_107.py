@gen_cluster(client=True)
async def test_no_startstops(c, s, a, b):
    tasks = TaskStreamPlugin(s)
    s.add_plugin(tasks)
    future = c.submit(inc, 1)
    await wait(future)
    assert len(tasks.buffer) == 1
    tasks.transition(future.key, 'processing', 'erred')
    assert len(tasks.buffer) == 1
    tasks.transition(future.key, 'processing', 'erred', startstops=[])
    assert len(tasks.buffer) == 1
    tasks.transition(future.key, 'processing', 'erred', startstops=[dict(start=time(), stop=time())])
    assert len(tasks.buffer) == 2