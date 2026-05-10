def hg_descriptor(f):
    """
  Return the histogram of oriented gradients descriptor.
  """
    wsx = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    wsy = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    f = f.astype(np.float64)
    fx = ndimage.convolve(f, wsx)
    fy = ndimage.convolve(f, wsy)
    N, M = f.shape
    div = np.sqrt(np.power(fx, 2) + np.power(fy, 2)).sum()
    Mg = np.sqrt(np.power(fx, 2) + np.power(fy, 2)) / div
    sigma = np.zeros(f.shape)
    sigma = np.arctan(fy / fx) + np.pi / 2
    sigma = np.degrees(sigma)
    sigma = np.digitize(sigma, np.arange(0, 180, 20))
    sigma = sigma.astype(np.uint8)
    dg = np.zeros(9)
    for x in range(N):
        for y in range(M):
            dg[sigma[x][y] - 1] += Mg[x][y]
    dg = dg / np.linalg.norm(dg)
    return dg