def interpolate(warp_file, lh_sphere):
    x = np.linspace(-128, 128, 256)
    y = np.linspace(0, 512, 512)
    warp = warp_file.squeeze()
    warp = warp.permute(0, 2, 1)
    warp = warp.detach().numpy()
    interpolate_function_x = RegularGridInterpolator((x, y), -warp[0])
    interpolate_function_y = RegularGridInterpolator((x, y), -warp[1])
    coords, faces = nib.freesurfer.read_geometry(lh_sphere)
    r, phi, theta = cartesian_to_spherical(coords[:, 0], coords[:, 1], coords[:, 2])
    p = phi.degree
    t = theta.degree
    theta_bins = 512
    phi_bins = 256
    theta_width = math.degrees(2 * np.pi) / theta_bins
    t /= theta_width
    phi_width = math.degrees(np.pi) / phi_bins
    p /= phi_width
    t = t.reshape(-1, 1)
    p = p.reshape(-1, 1)
    pts = np.concatenate((p, t), axis=1)
    new_pts_x = interpolate_function_x(pts)
    new_pts_y = interpolate_function_y(pts)
    x_prime = pts.T[0] + new_pts_x
    y_prime = pts.T[1] + new_pts_y
    x_prime *= phi_width
    y_prime *= theta_width
    y_prime = np.clip(y_prime, 0, 360)
    x_prime = np.clip(x_prime, -90, 90)
    t_prime = [math.radians(i) for i in y_prime]
    p_prime = [math.radians(i) for i in x_prime]
    t_prime = np.array(t_prime)
    p_prime = np.array(p_prime)
    return (r, p_prime, t_prime)