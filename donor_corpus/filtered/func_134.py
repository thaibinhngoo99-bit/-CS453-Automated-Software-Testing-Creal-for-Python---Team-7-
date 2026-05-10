def oda_update_uhf(dFs, dDs, dE):
    """
    ODA update:
        lbd = 0.5 - dE / E_deriv
    """
    if type(dFs) is not list:
        raise Exception('arg1 and arg2 are list of alpha/beta matrices.')
    E_deriv = np.sum(dFs[0] * dDs[0] + dFs[1] * dDs[1])
    lbd = 0.5 * (1.0 - dE / E_deriv)
    if lbd < 0 or lbd > 1:
        lbd = 0.9999 if dE < 0 else 0.0001
    return lbd