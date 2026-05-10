def test_pin_names_1():
    codec = Part('xess.lib', 'ak4520a')
    assert codec['ain'] == codec.n['ain']
    assert codec[1:4] == codec.p[1:4]