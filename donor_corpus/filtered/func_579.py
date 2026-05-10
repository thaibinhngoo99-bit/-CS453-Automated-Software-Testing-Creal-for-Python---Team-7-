def analyze_regression(args, test_data, cortical_result, dist_results):
    hidd_dists = dist_results['hidd_dists']
    grid_dists = dist_results['grid_dists']
    phi = dist_results['angle_results']['phi']
    binary_phi = dist_results['angle_results']['binary_phi']
    x_cat = np.concatenate((grid_dists.reshape((-1, 1)), binary_phi.reshape((-1, 1))), axis=1)
    x_con = np.concatenate((grid_dists.reshape((-1, 1)), phi.reshape((-1, 1))), axis=1)
    x_cat = sm.add_constant(x_cat)
    if args.cortical_model == 'stepwisemlp':
        p_val, t_val, param, bse = ([[] for i in range(2)] for i in range(4))
        y_hat_E = np.zeros(hidd_dists.shape)
        y = np.zeros(hidd_dists.shape)
        for h in range(2):
            y[:, h] = hidd_dists[:, h]
            y_hat_E[:, h], p_val[h], t_val[h], param[h], bse[h] = run_regression(x_cat, y[:, h], grid_dists)
    else:
        y = hidd_dists
        y_hat_E, p_val, t_val, param, bse = run_regression(x_cat, y, grid_dists)
    cat_reg = {'p_val': p_val, 't_val': t_val, 'param': param, 'y_hat_E': y_hat_E, 'y': y, 'bse': bse}
    x_con = sm.add_constant(x_con)
    if args.cortical_model == 'stepwisemlp':
        p_val, t_val, param, bse = ([[] for i in range(2)] for i in range(4))
        y_hat_E = np.zeros(hidd_dists.shape)
        y = np.zeros(hidd_dists.shape)
        for h in range(2):
            y[:, h] = hidd_dists[:, h]
            y_hat_E[:, h], p_val[h], t_val[h], param[h], bse[h] = run_regression(x_con, y[:, h], grid_dists)
    else:
        y = hidd_dists
        y_hat_E, p_val, t_val, param, bse = run_regression(x_con, y, grid_dists)
    con_reg = {'p_val': p_val, 't_val': t_val, 'param': param, 'y_hat_E': y_hat_E, 'y': y, 'bse': bse}
    reg_results = {'cat_reg': cat_reg, 'con_reg': con_reg}
    return reg_results