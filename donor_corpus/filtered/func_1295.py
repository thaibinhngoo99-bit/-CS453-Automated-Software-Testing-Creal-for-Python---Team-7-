def get_all_boxes(coords, pad=5):
    """Get all pocket boxes for protein coords.

  We pad all boxes the prescribed number of angstroms.

  TODO(rbharath): It looks like this may perhaps be non-deterministic?
  """
    hull = ConvexHull(coords)
    boxes = []
    for triangle in hull.simplices:
        points = np.array([coords[triangle, 0], coords[triangle, 1], coords[triangle, 2]]).T
        x_min, x_max = (np.amin(points[:, 0]), np.amax(points[:, 0]))
        x_min, x_max = (int(np.floor(x_min)) - pad, int(np.ceil(x_max)) + pad)
        y_min, y_max = (np.amin(points[:, 1]), np.amax(points[:, 1]))
        y_min, y_max = (int(np.floor(y_min)) - pad, int(np.ceil(y_max)) + pad)
        z_min, z_max = (np.amin(points[:, 2]), np.amax(points[:, 2]))
        z_min, z_max = (int(np.floor(z_min)) - pad, int(np.ceil(z_max)) + pad)
        boxes.append(((x_min, x_max), (y_min, y_max), (z_min, z_max)))
    return boxes