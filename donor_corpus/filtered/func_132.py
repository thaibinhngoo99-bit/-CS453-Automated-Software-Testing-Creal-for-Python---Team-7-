def get_fock_uhf(H, g, Ds):
    """
    DIIS update given previous Fock matrices and error vectors.
    Note that if there are less than two F's, return normal F.
    """
    Jtot, Ka, Kb = get_JK_uhf(len(g.shape) == 3, g, Ds)
    return (H + Jtot - Ka, H + Jtot - Kb)