def analyze_regression_1D(args, test_data, cortical_result, dist_results):
    hidd_dists_ctxs = dist_results['hidd_dists_ctxs']
    hidd_dists_ctx0 = hidd_dists_ctxs[0]
    hidd_dists_ctx1 = hidd_dists_ctxs[1]
    grid_1ds_ctxs = dist_results['grid_1ds_ctxs']
    grid_1ds_ctx0 = grid_1ds_ctxs[0]
    grid_1ds_ctx1 = grid_1ds_ctxs[1]
    grid_dists = dist_results['grid_dists']
    phi = dist_results['angle_results']['phi']
    binary_phi = dist_results['angle_results']['binary_phi']
    hidd_dists_ctx = np.concatenate((hidd_dists_ctx0, hidd_dists_ctx1), axis=0)
    grid_1ds_ctx = np.concatenate((grid_1ds_ctx0, grid_1ds_ctx1), axis=0)
    grid_dists_ctx = np.concatenate((grid_dists, grid_dists), axis=0)
    binary_phi_ctx = np.concatenate((binary_phi, binary_phi), axis=0)
    phi_ctx = np.concatenate((phi, phi), axis=0)
    x_cat = np.concatenate((grid_dists_ctx.reshape((-1, 1)), grid_1ds_ctx.reshape((-1, 1)), binary_phi_ctx.reshape((-1, 1))), axis=1)
    x_con = np.concatenate((grid_dists_ctx.reshape((-1, 1)), grid_1ds_ctx.reshape((-1, 1)), phi_ctx.reshape((-1, 1))), axis=1)
    x_cat = sm.add_constant(x_cat)
    if args.cortical_model == 'stepwisemlp':
        p_val, t_val, param, y_hat_E, y, bse = ([[] for i in range(2)] for i in range(6))
        y_hat_E = np.zeros(hidd_dists_ctx.shape)
        y = np.zeros(hidd_dists_ctx.shape)
        for h in range(2):
            y[:, h] = hidd_dists_ctx[:, h]
            y_hat_E[:, h], p_val[h], t_val[h], param[h], bse[h] = run_regression(x_cat, y[:, h], grid_dists_ctx)
    else:
        y = hidd_dists_ctx
        y_hat_E, p_val, t_val, param, bse = run_regression(x_cat, y, grid_dists_ctx)
    cat_reg = {'p_val': p_val, 't_val': t_val, 'param': param, 'y_hat_E': y_hat_E, 'y': y, 'bse': bse}
    x_con = sm.add_constant(x_con)
    if args.cortical_model == 'stepwisemlp':
        p_val, t_val, param, bse = ([[] for i in range(2)] for i in range(4))
        y_hat_E = np.zeros(hidd_dists_ctx.shape)
        y = np.zeros(hidd_dists_ctx.shape)
        for h in range(2):
            y[:, h] = hidd_dists_ctx[:, h]
            y_hat_E[:, h], p_val[h], t_val[h], param[h], bse[h] = run_regression(x_con, y[:, h], grid_dists_ctx)
    else:
        y = hidd_dists_ctx
        y_hat_E, p_val, t_val, param, bse = run_regression(x_con, y, grid_dists_ctx)
    con_reg = {'p_val': p_val, 't_val': t_val, 'param': param, 'y_hat_E': y_hat_E, 'y': y, 'bse': bse}
    reg_results = {'cat_reg': cat_reg, 'con_reg': con_reg}
    return reg_results