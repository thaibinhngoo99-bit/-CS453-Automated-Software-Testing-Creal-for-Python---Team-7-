def xyz2degree(lh_sphere, lh_sulc):
    coords, faces = nib.freesurfer.read_geometry(lh_sphere)
    r, phi, theta = cartesian_to_spherical(coords[:, 0], coords[:, 1], coords[:, 2])
    lat = phi.degree + 90
    lon = theta.degree
    y_bins = 512
    x_bins = 256
    y_width = math.degrees(2 * np.pi) / y_bins
    ys = lon // y_width
    x_width = math.degrees(np.pi) / x_bins
    xs = lat // x_width
    ys = np.clip(ys, 0, 511)
    xs = np.clip(xs, 0, 255)
    lh_morph_sulc = nib.freesurfer.read_morph_data(lh_sulc)
    xs = xs.astype(np.int32)
    ys = ys.astype(np.int32)
    values = np.zeros((512, 256))
    values[ys, xs] = lh_morph_sulc
    return values