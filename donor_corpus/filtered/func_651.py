@pytest.mark.parametrize('lock', [True, False])
@pytest.mark.parametrize('asarray', [True, False])
@pytest.mark.parametrize('fancy', [True, False])
def test_gh4043(lock, asarray, fancy):
    a1 = da.from_array(np.zeros(3), chunks=1, asarray=asarray, lock=lock, fancy=fancy)
    a2 = da.from_array(np.ones(3), chunks=1, asarray=asarray, lock=lock, fancy=fancy)
    al = da.stack([a1, a2])
    assert_eq(al, al)