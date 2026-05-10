def xiquadpole(correlsmu, mu):
    xi4 = np.sum(9.0 * correlsmu * sp.special.legendre(4)(mu), axis=1) / len(mu)
    np.savetxt('xi4.txt', xi4)
    return xi4