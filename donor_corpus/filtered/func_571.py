def calc_dist_ctx(args, test_data, cortical_result, dist_results):
    N_contexts = 2
    n_states = test_data.n_states
    loc2idx = test_data.loc2idx
    idx2loc = {idx: loc for loc, idx in loc2idx.items()}
    idxs = [idx for idx in range(n_states)]
    N_contexts = args.N_contexts
    N_responses = args.N_responses
    avg_hidden_ctxs = cortical_result['avg_hidden_ctxs']
    grid_dists = []
    hidd_dists_ctxs = [[] for i in range(N_contexts)]
    grid_1ds_ctxs = [[] for i in range(N_contexts)]
    grid_angles = []
    samples = []
    for idx1, idx2 in combinations(idxs, 2):
        (x1, y1), (x2, y2) = (idx2loc[idx1], idx2loc[idx2])
        samples.append((idx1, idx2))
        grid_dist = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        grid_dists.append(grid_dist)
        for ctx in range(N_contexts):
            if args.cortical_model == 'stepwisemlp':
                hidd_dist = np.zeros([2])
                hidd1, hidd2 = (avg_hidden_ctxs[0, ctx, idx1, :], avg_hidden_ctxs[0, ctx, idx2, :])
                hidd_dist[0] = np.linalg.norm(hidd1 - hidd2)
                hidd1, hidd2 = (avg_hidden_ctxs[1, ctx, idx1, :], avg_hidden_ctxs[1, ctx, idx2, :])
                hidd_dist[1] = np.linalg.norm(hidd1 - hidd2)
            else:
                hidd1, hidd2 = (avg_hidden_ctxs[ctx][idx1], avg_hidden_ctxs[ctx][idx2])
                hidd_dist = np.linalg.norm(hidd1 - hidd2)
            hidd_dists_ctxs[ctx].append(hidd_dist)
            loc1 = [x1, y1]
            loc2 = [x2, y2]
            winegrid = WineGrid(N_responses, N_contexts)
            r1, r2 = winegrid.ctx_to_r(ctx, loc1, loc2)
            grid_1ds_ctxs[ctx].append(np.abs(r1 - r2))
        grid_angle = np.arctan2(y2 - y1, x2 - x1)
        grid_angles.append(grid_angle)
    grid_dists = np.array(grid_dists)
    grid_angles = np.array(grid_angles)
    samples = np.array(samples)
    hidd_dists_ctxs = np.array(hidd_dists_ctxs)
    phi = np.sin(2 * grid_angles)
    binary_phi = np.sign(phi)
    for i, p in enumerate(phi):
        if np.abs(p) < 1e-05:
            binary_phi[i] = 0
    angle_results = {'grid_angles': grid_angles, 'phi': phi, 'binary_phi': binary_phi}
    dist_results = {'samples': samples, 'hidd_dists_ctxs': hidd_dists_ctxs, 'grid_1ds_ctxs': grid_1ds_ctxs, 'grid_dists': grid_dists, 'angle_results': angle_results}
    return dist_results