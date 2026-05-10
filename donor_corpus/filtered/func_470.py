@njit(output_type_log2(int64[:], int64[:, :], int64[:], int64[:, :], float64[:, :], float64[:, :, :], float64[:, :, :], int64), cache=True)
def _logbp_numba_regular(bits_hist, bits_values, nodes_hist, nodes_values, Lc, Lq, Lr, n_iter):
    """Perform inner ext LogBP solver."""
    m, n, n_messages = Lr.shape
    for i in range(m):
        ni = bits_values[i]
        for j in ni:
            nij = ni[:]
            X = np.ones(n_messages)
            if n_iter == 0:
                for kk in range(len(nij)):
                    if nij[kk] != j:
                        X *= np.tanh(0.5 * Lc[nij[kk]])
            else:
                for kk in range(len(nij)):
                    if nij[kk] != j:
                        X *= np.tanh(0.5 * Lq[i, nij[kk]])
            num = 1 + X
            denom = 1 - X
            for ll in range(n_messages):
                if num[ll] == 0:
                    Lr[i, j, ll] = -1
                elif denom[ll] == 0:
                    Lr[i, j, ll] = 1
                else:
                    Lr[i, j, ll] = np.log(num[ll] / denom[ll])
    for j in range(n):
        mj = nodes_values[j]
        for i in mj:
            mji = mj[:]
            Lq[i, j] = Lc[j]
            for kk in range(len(mji)):
                if mji[kk] != i:
                    Lq[i, j] += Lr[mji[kk], j]
    L_posteriori = np.zeros((n, n_messages))
    for j in range(n):
        mj = nodes_values[j]
        L_posteriori[j] = Lc[j] + Lr[mj, j].sum(axis=0)
    return (Lq, Lr, L_posteriori)