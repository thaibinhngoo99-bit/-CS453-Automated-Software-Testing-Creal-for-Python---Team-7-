def oda_update(dF, dD, dE):
    """
    ODA update:
        lbd = 0.5 - dE / E_deriv
    """
    E_deriv = np.sum(dF * dD)
    lbd = 0.5 * (1.0 - dE / E_deriv)
    if lbd < 0 or lbd > 1:
        lbd = 0.9999 if dE < 0 else 0.0001
    return lbd