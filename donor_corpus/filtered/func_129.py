def get_JK_uhf(is_fitted, g, Ds):
    """
    Ds = [Da, Db]
    """
    Da, Db = (Ds[0], Ds[1])
    Dtot = Da + Db
    if is_fitted == True:
        X = np.einsum('Pls,ls->P', g, Dtot)
        Jtot = np.einsum('mnP,P->mn', np.swapaxes(g, 0, 2), X)
        Za = np.einsum('Pns,ls->Pnl', g, Da)
        Ka = np.einsum('mlP,Pnl->mn', np.swapaxes(g, 0, 2), Za)
        Zb = np.einsum('Pns,ls->Pnl', g, Db)
        Kb = np.einsum('mlP,Pnl->mn', np.swapaxes(g, 0, 2), Zb)
        return (Jtot, Ka, Kb)
    else:
        Jtot = np.einsum('pqrs, rs -> pq', g, Dtot)
        Ka = np.einsum('prqs, rs -> pq', g, Da)
        Kb = np.einsum('prqs, rs -> pq', g, Db)
        return (Jtot, Ka, Kb)