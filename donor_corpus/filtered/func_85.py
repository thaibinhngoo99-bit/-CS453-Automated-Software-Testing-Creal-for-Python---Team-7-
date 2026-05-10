def luminance(img):
    """
  Get a RGB image as input and return a black&white image.
  """
    N, M, _ = img.shape
    out = np.empty(img.shape)
    out = 0.299 * img[:, :, 0] + 0.587 * img[:, :, 1] + 0.114 * img[:, :, 2]
    return out.astype(np.uint8)