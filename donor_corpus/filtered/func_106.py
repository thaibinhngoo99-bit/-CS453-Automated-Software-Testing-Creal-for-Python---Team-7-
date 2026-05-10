@gen_cluster(client=True)
async def test_collect(c, s, a, b):
    tasks = TaskStreamPlugin(s)
    s.add_plugin(tasks)
    start = time()
    futures = c.map(slowinc, range(10), delay=0.1)
    await wait(futures)
    L = tasks.collect()
    assert len(L) == len(futures)
    L = tasks.collect(start=start)
    assert len(L) == len(futures)
    L = tasks.collect(start=start + 0.2)
    assert 4 <= len(L) <= len(futures)
    L = tasks.collect(start='20 s')
    assert len(L) == len(futures)
    L = tasks.collect(start='500ms')
    assert 0 < len(L) <= len(futures)
    L = tasks.collect(count=3)
    assert len(L) == 3
    assert L == list(tasks.buffer)[-3:]
    assert tasks.collect(stop=start + 100, count=3) == tasks.collect(count=3)
    assert tasks.collect(start=start, count=3) == list(tasks.buffer)[:3]