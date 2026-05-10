def init_state_is_array(init_state):
    """
    Checks whether init_state is compliant with an Nd algorithm.
    That is, whether init_state is an (d,) np.ndarray.
    """
    assert isinstance(init_state, np.ndarray), 'Please enter init_state of shape (d,)'
    assert len(init_state.shape) == 1, 'Please enter init_state of shape (d,)'
    return True