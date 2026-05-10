def analyze_ttest(args, test_data, cortical_result, dist_results):
    cong_res = dist_results['cong_dist_results']
    incong_res = dist_results['incong_dist_results']
    incong_hidd_dists = incong_res['incong_hidd_dists']
    cong_hidd_dists = cong_res['cong_hidd_dists']
    if args.cortical_model == 'stepwisemlp':
        t_hidd, t_p_val_hidd = (np.zeros([2]), np.zeros([2]))
        for h in range(2):
            t_hidd[h], t_p_val_hidd[h] = ttest_ind(cong_hidd_dists[:, h], incong_hidd_dists[:, h])
    else:
        t_hidd, t_p_val_hidd = ttest_ind(cong_res['cong_hidd_dists'], incong_res['incong_hidd_dists'])
    t_embed, t_p_val_embed = ttest_ind(cong_res['cong_embed_dists'], incong_res['incong_embed_dists'])
    t_grid, t_p_val_grid = ttest_ind(cong_res['cong_grid_dists'], incong_res['incong_grid_dists'])
    ttest_results = {'t_stat_hidd': t_hidd, 't_p_val_hidd': t_p_val_hidd, 't_stat_embed': t_embed, 't_p_val_embed': t_p_val_embed, 't_grid': t_grid, 't_p_val_grid': t_p_val_grid}
    return ttest_results