def test_RFC3339():
    ts = wt.kit.TimeStamp()
    assert ts.RFC3339
    assert wt.kit.timestamp_from_RFC3339(ts.RFC3339) == ts