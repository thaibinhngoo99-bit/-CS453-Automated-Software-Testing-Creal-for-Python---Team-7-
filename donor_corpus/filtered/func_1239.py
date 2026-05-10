def xidipole(correlsmu, mu):
    xi2 = np.sum(5.0 * correlsmu * sp.special.legendre(2)(mu), axis=1) / len(mu)
    np.savetxt('xi2.txt', xi2)
    return xi2