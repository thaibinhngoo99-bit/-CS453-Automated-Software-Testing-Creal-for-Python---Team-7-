def analyze_corr(args, test_data, cortical_result, dist_results):
    grid_dists = dist_results['grid_dists']
    embed_dists = dist_results['embed_dists']
    hidd_dists = dist_results['hidd_dists']
    cong_res = dist_results['cong_dist_results']
    incong_res = dist_results['incong_dist_results']
    r_embed, p_val_embed = pearsonr(grid_dists, embed_dists)
    if args.cortical_model == 'stepwisemlp':
        r_hidd, p_val_hidd = (np.zeros([2]), np.zeros([2]))
        r_cong_hidd, p_val_cong_hidd, r_incong_hidd, p_val_incong_hidd = (np.zeros([2]), np.zeros([2]), np.zeros([2]), np.zeros([2]))
        cong_hidd_dists, incong_hidd_dists = (cong_res['cong_hidd_dists'], incong_res['incong_hidd_dists'])
        for h in range(2):
            r_hidd[h], p_val_hidd[h] = pearsonr(grid_dists, hidd_dists[:, h])
            r_cong_hidd[h], p_val_cong_hidd[h] = pearsonr(cong_res['cong_grid_dists'], cong_hidd_dists[:, h])
            r_incong_hidd[h], p_val_incong_hidd[h] = pearsonr(incong_res['incong_grid_dists'], incong_hidd_dists[:, h])
    else:
        r_hidd, p_val_hidd = pearsonr(grid_dists, hidd_dists)
        r_cong_hidd, p_val_cong_hidd = pearsonr(cong_res['cong_grid_dists'], cong_res['cong_hidd_dists'])
        r_incong_hidd, p_val_incong_hidd = pearsonr(incong_res['incong_grid_dists'], incong_res['incong_hidd_dists'])
    r_cong_embed, p_val_cong_embed = pearsonr(cong_res['cong_grid_dists'], cong_res['cong_embed_dists'])
    r_incong_embed, p_val_incong_embed = pearsonr(incong_res['incong_grid_dists'], incong_res['incong_embed_dists'])
    corr_results = {'r_embed': r_embed, 'p_val_embed': p_val_embed, 'r_cong_embed': r_cong_embed, 'p_val_cong_embed': p_val_cong_embed, 'r_incong_embed': r_incong_embed, 'p_val_incong_embed': p_val_incong_embed, 'r_hidd': r_hidd, 'p_val_hidd': p_val_hidd, 'r_cong_hidd': r_cong_hidd, 'p_val_cong_hidd': p_val_cong_hidd, 'r_incong_hidd': r_incong_hidd, 'p_val_incong_hidd': p_val_incong_hidd}
    return corr_results