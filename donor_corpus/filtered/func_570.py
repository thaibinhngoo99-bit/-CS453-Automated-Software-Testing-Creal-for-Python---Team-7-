def proportions(args, test_data, cortical_result, dist_results):
    hiddens_ctxs = cortical_result['hiddens_ctxs']
    hiddens_ctxs = [np.concatenate(h, axis=0) for h in hiddens_ctxs]
    ps = []
    p_pies = []
    for h in hiddens_ctxs:
        p_pies.append(np.any(h > 0, axis=0))
        ps.append(np.mean(h > 0, axis=0))
    ps = np.asarray(ps)
    s = np.sum(ps, axis=0, keepdims=True)
    n = ps / s
    prop_results = {'hiddens_ctxs': hiddens_ctxs, 'p_pies': p_pies, 'ps': ps, 'n': n}
    return prop_results