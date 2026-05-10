def ht_descriptor(f):
    """
  Return the Haralick texture descriptors (intensity-level co-ocurrence matrix).
  """
    N, M = f.shape
    C = np.zeros((LEVELS, LEVELS))
    for x in range(N - 1):
        for y in range(M - 1):
            i = f[x, y]
            j = f[x + 1, y + 1]
            C[i][j] += 1
    C = C / C.sum()
    N, M = C.shape
    energy = np.power(C, 2).sum()
    epsilon = 0.001
    entropy = -(C * np.log(C + epsilon)).sum()
    A = np.fromfunction(lambda i, j: (i - j) ** 2, (N, M), dtype=int)
    contrast = 1 / math.pow(N, 2) * (C * A).sum()
    mu_i, si_i = (0, 0)
    mu_j, si_j = (0, 0)
    for k in range(N):
        a1 = C[k, :].sum()
        mu_i += k * a1
        si_i += math.pow(k - mu_i, 2) * a1
        a2 = C[:, k].sum()
        mu_j += k * a2
        si_j += math.pow(k - mu_j, 2) * a2
    A = np.fromfunction(lambda i, j: (i - j) ** 2, (N, M), dtype=int)
    correlation = (A * C).sum() - mu_i * mu_j
    correlation /= si_i * si_j
    homogeneity = 0
    A = np.fromfunction(lambda i, j: 1 + abs(i - j), (N, M), dtype=int)
    homogeneity = (C * A).sum()
    dt = np.array([energy, entropy, contrast, correlation, homogeneity])
    dt = dt / np.linalg.norm(dt)
    return dt