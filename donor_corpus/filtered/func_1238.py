def ximonopole(correlsmu, mu):
    xi0 = np.sum(correlsmu * sp.special.legendre(0)(mu), axis=1) / len(mu)
    np.savetxt('xi0.txt', xi0)
    return xi0