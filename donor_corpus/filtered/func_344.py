def test_pin_names_2():
    codec = Part('xess.lib', 'ak4520a')
    codec[4].name = 'A1'
    codec[8].name = 'A2'
    codec[8].num = 'A1'
    assert codec[4] is codec.n['A1']
    assert codec.p[4] is codec.n['A1']
    assert codec[4] is codec.p[4]
    assert codec.p['A1'] is codec.n['A2']
    assert codec['A1'] is codec.n['A2']
    assert codec['A1'] is codec.p['A1']