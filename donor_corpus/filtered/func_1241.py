def beta(correlsmu, mu):
    xis0 = ximonopole(correlsmu, mu)
    xis2 = xidipole(correlsmu, mu)
    xis4 = xiquadpole(correlsmu, mu)
    xir = xis0 * sp.special.legendre(0)(mu) + xis2 * sp.special.legendre(2)(mu) + xis4 * sp.special.legendre(4)(mu)
    r = xir / xis0
    return 5.0 / 3.0 * (np.sqrt(1.8 * r - 0.8) - 1.0)