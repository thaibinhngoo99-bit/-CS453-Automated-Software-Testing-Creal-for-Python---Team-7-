def analyze_regression_exc(args, test_data, cortical_result, dist_results):
    n_states = test_data.n_states
    hidd_dists = dist_results['hidd_dists']
    grid_dists = dist_results['grid_dists']
    binary_phi = dist_results['angle_results']['binary_phi']
    samples = dist_results['samples']
    states = []
    if args.cortical_model == 'stepwisemlp':
        p_vals, t_vals, params, bses = ([[] for i in range(2)] for i in range(4))
    else:
        p_vals, t_vals, params, bses = ([] for i in range(4))
    for state in range(n_states):
        s_idxs = [i for i, sample in enumerate(samples) if state not in sample]
        x_cat = np.concatenate((grid_dists[s_idxs].reshape((-1, 1)), binary_phi[s_idxs].reshape((-1, 1))), axis=1)
        x_cat = sm.add_constant(x_cat)
        if args.cortical_model == 'stepwisemlp':
            for h in range(2):
                y = hidd_dists[s_idxs, h]
                _, p_val, t_val, param, bse = run_regression(x_cat, y, grid_dists)
                p_vals[h].append(p_val)
                t_vals[h].append(t_val)
                params[h].append(param)
                bses[h].append(bse)
        else:
            y = hidd_dists[s_idxs]
            _, p_val, t_val, param, bse = run_regression(x_cat, y, grid_dists)
            p_vals.append(p_val)
            t_vals.append(t_val)
            params.append(param)
            bses.append(bse)
        states.append(state)
    s_idxs = [i for i, sample in enumerate(samples) if (0 not in sample) & (15 not in sample)]
    x_cat = np.concatenate((grid_dists[s_idxs].reshape((-1, 1)), binary_phi[s_idxs].reshape((-1, 1))), axis=1)
    x_cat = sm.add_constant(x_cat)
    if args.cortical_model == 'stepwisemlp':
        for h in range(2):
            y = hidd_dists[s_idxs, h]
            _, p_val, t_val, param, bse = run_regression(x_cat, y, grid_dists)
            p_vals[h].append(p_val)
            t_vals[h].append(t_val)
            params[h].append(param)
            bses[h].append(bse)
    else:
        y = hidd_dists[s_idxs]
        _, p_val, t_val, param, bse = run_regression(x_cat, y, grid_dists)
        p_vals.append(p_val)
        t_vals.append(t_val)
        params.append(param)
        bses.append(bse)
    states.append(16)
    s_idxs = [i for i, sample in enumerate(samples) if (0 not in sample) & (15 not in sample) & (3 not in sample) & (12 not in sample)]
    x_cat = np.concatenate((grid_dists[s_idxs].reshape((-1, 1)), binary_phi[s_idxs].reshape((-1, 1))), axis=1)
    x_cat = sm.add_constant(x_cat)
    if args.cortical_model == 'stepwisemlp':
        for h in range(2):
            y = hidd_dists[s_idxs, h]
            _, p_val, t_val, param, bse = run_regression(x_cat, y, grid_dists)
            p_vals[h].append(p_val)
            t_vals[h].append(t_val)
            params[h].append(param)
            bses[h].append(bse)
    else:
        y = hidd_dists[s_idxs]
        _, p_val, t_val, param, bse = run_regression(x_cat, y, grid_dists)
        p_vals.append(p_val)
        t_vals.append(t_val)
        params.append(param)
        bses.append(bse)
    states.append(17)
    states = np.array(states)
    p_vals = np.array(p_vals)
    t_vals = np.array(t_vals)
    params = np.array(params)
    bses = np.array(bses)
    exc_reg_results = {'excluded_states': states, 'p_vals': p_vals, 't_vals': t_vals, 'params': params, 'bses': bses}
    return exc_reg_results