@gen_cluster(client=True)
async def test_maxlen(c, s, a, b):
    tasks = TaskStreamPlugin(s, maxlen=5)
    s.add_plugin(tasks)
    futures = c.map(inc, range(10))
    await wait(futures)
    assert len(tasks.buffer) == 5