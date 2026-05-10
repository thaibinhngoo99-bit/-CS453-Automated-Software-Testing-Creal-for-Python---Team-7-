def test_step():
    model = Model(nswimmers=1)
    swimmer = copy.deepcopy(model.swimmers[0])
    dt = 1
    swimmer.swim(dt)
    model.step(dt)
    assert swimmer.pos == model.swimmers[0].pos