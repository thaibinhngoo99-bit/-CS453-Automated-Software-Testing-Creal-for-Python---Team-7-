def homo_lumo_mix(C, nocc, beta):
    """
    Mix a portion of LUMO to HOMO.
    Used when generating spin-unrestricted guess.
    """
    if beta < 0.0 or beta > 1.0:
        raise Exception('Mixing beta must be in [0, 1]')
    Cb = C.copy()
    homo = C[:, nocc - 1]
    lumo = C[:, nocc]
    Cb[:, nocc - 1] = (1.0 - beta) ** 0.5 * homo + beta ** 0.5 * lumo
    return Cb