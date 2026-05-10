@gen_cluster(client=True)
async def test_client(c, s, a, b):
    L = await c.get_task_stream()
    assert L == ()
    futures = c.map(slowinc, range(10), delay=0.1)
    await wait(futures)
    tasks = s.plugins[TaskStreamPlugin.name]
    L = await c.get_task_stream()
    assert L == tuple(tasks.buffer)