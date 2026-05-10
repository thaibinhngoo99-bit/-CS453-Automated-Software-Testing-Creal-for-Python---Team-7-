def calc_dist(args, test_data, cortical_result, dist_results=None):
    n_states = test_data.n_states
    loc2idx = test_data.loc2idx
    idx2loc = {idx: loc for loc, idx in loc2idx.items()}
    idxs = [idx for idx in range(n_states)]
    grid_dists = []
    cong_grid_dists = []
    incong_grid_dists = []
    embed_dists = []
    hidd_dists = []
    cong_hidd_dists = []
    incong_hidd_dists = []
    cong_embed_dists = []
    incong_embed_dists = []
    grid_angles = []
    cong_grid_angles = []
    incong_grid_angles = []
    samples = []
    embeddings = cortical_result['embeddings']
    avg_hidden = cortical_result['avg_hidden']
    for idx1, idx2 in combinations(idxs, 2):
        (x1, y1), (x2, y2) = (idx2loc[idx1], idx2loc[idx2])
        samples.append((idx1, idx2))
        grid_dist = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        grid_dists.append(grid_dist)
        emb1, emb2 = (embeddings[idx1], embeddings[idx2])
        embed_dist = np.linalg.norm(emb1 - emb2)
        embed_dists.append(embed_dist)
        if args.cortical_model == 'stepwisemlp':
            hidd_dist = np.zeros([2])
            hidd1, hidd2 = (avg_hidden[0, idx1], avg_hidden[0, idx2])
            hidd_dist[0] = np.linalg.norm(hidd1 - hidd2)
            hidd1, hidd2 = (avg_hidden[1, idx1], avg_hidden[1, idx2])
            hidd_dist[1] = np.linalg.norm(hidd1 - hidd2)
        else:
            hidd1, hidd2 = (avg_hidden[idx1], avg_hidden[idx2])
            hidd_dist = np.linalg.norm(hidd1 - hidd2)
        hidd_dists.append(hidd_dist)
        grid_angle = np.arctan2(y2 - y1, x2 - x1)
        grid_angles.append(grid_angle)
        phi = np.sin(2 * grid_angle)
        if np.abs(phi) < 1e-05:
            cong = 0
        else:
            cong = np.sign(phi)
        if cong == 1:
            cong_hidd_dists.append(hidd_dist)
            cong_grid_dists.append(grid_dist)
            cong_embed_dists.append(embed_dist)
            cong_grid_angles.append(grid_angle)
        if cong == -1:
            incong_hidd_dists.append(hidd_dist)
            incong_grid_dists.append(grid_dist)
            incong_embed_dists.append(embed_dist)
            incong_grid_angles.append(grid_angle)
    grid_dists = np.array(grid_dists)
    embed_dists = np.array(embed_dists)
    hidd_dists = np.array(hidd_dists)
    cong_grid_dists = np.array(cong_grid_dists)
    incong_grid_dists = np.array(incong_grid_dists)
    cong_hidd_dists = np.array(cong_hidd_dists)
    incong_hidd_dists = np.array(incong_hidd_dists)
    cong_embed_dists = np.array(cong_embed_dists)
    incong_embed_dists = np.array(incong_embed_dists)
    grid_angles = np.array(grid_angles)
    cong_grid_angles = np.array(cong_grid_angles)
    incong_grid_angles = np.array(incong_grid_angles)
    samples = np.array(samples)
    phi = np.sin(2 * grid_angles)
    binary_phi = np.sign(phi)
    for i, p in enumerate(phi):
        if np.abs(p) < 1e-05:
            binary_phi[i] = 0
    cong_dist_results = {'cong_grid_dists': cong_grid_dists, 'cong_hidd_dists': cong_hidd_dists, 'cong_embed_dists': cong_embed_dists}
    incong_dist_results = {'incong_grid_dists': incong_grid_dists, 'incong_hidd_dists': incong_hidd_dists, 'incong_embed_dists': incong_embed_dists}
    angle_results = {'grid_angles': grid_angles, 'cong_grid_angles': cong_grid_angles, 'incong_grid_angles': incong_grid_angles, 'phi': phi, 'binary_phi': binary_phi}
    dist_results = {'samples': samples, 'grid_dists': grid_dists, 'embed_dists': embed_dists, 'hidd_dists': hidd_dists, 'cong_dist_results': cong_dist_results, 'incong_dist_results': incong_dist_results, 'angle_results': angle_results}
    return dist_results