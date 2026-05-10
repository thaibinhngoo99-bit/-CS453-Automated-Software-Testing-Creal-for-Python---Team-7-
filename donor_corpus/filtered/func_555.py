@pytest.fixture()
def pars():
    x = Parameter('x', 2.1)
    y = Parameter('y', 3.1, scale=100000.0)
    z = Parameter('z', 4.1, scale=1e-05)
    return Parameters([x, y, z])