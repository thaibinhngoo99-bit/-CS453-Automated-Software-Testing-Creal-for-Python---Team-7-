def decode(H, y, snr, maxiter=1000):
    """Decode a Gaussian noise corrupted n bits message using BP algorithm.

    Decoding is performed in parallel if multiple codewords are passed in y.

    Parameters
    ----------
    H: array (n_equations, n_code). Decoding matrix H.
    y: array (n_code, n_messages) or (n_code,). Received message(s) in the
        codeword space.
    maxiter: int. Maximum number of iterations of the BP algorithm.

    Returns
    -------
    x: array (n_code,) or (n_code, n_messages) the solutions in the
        codeword space.

    """
    m, n = H.shape
    bits_hist, bits_values, nodes_hist, nodes_values = utils._bitsandnodes(H)
    _n_bits = np.unique(H.sum(0))
    _n_nodes = np.unique(H.sum(1))
    if _n_bits * _n_nodes == 1:
        solver = _logbp_numba_regular
        bits_values = bits_values.reshape(n, -1)
        nodes_values = nodes_values.reshape(m, -1)
    else:
        solver = _logbp_numba
    var = 10 ** (-snr / 10)
    if y.ndim == 1:
        y = y[:, None]
    Lc = 2 * y / var
    _, n_messages = y.shape
    Lq = np.zeros(shape=(m, n, n_messages))
    Lr = np.zeros(shape=(m, n, n_messages))
    for n_iter in range(maxiter):
        Lq, Lr, L_posteriori = solver(bits_hist, bits_values, nodes_hist, nodes_values, Lc, Lq, Lr, n_iter)
        x = np.array(L_posteriori <= 0).astype(int)
        product = utils.incode(H, x)
        if product:
            break
    if n_iter == maxiter - 1:
        warnings.warn('Decoding stopped before convergence. You may want\n                       to increase maxiter')
    return x.squeeze()