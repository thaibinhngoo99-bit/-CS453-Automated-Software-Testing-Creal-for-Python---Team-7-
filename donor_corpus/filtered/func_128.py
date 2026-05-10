def get_dm(C, nel):
    D = C[:, :nel]
    D = D @ D.T
    return D