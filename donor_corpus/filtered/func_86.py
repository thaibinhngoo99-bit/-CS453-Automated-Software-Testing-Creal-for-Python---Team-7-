def nh_descriptor(f):
    """
  Return the normalized histogram descriptor.
  """
    hist, _ = np.histogram(f, bins=[i for i in range(2 ** b + 1)])
    hist = hist / hist.sum()
    dc = hist / np.linalg.norm(hist)
    return dc