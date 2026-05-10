def hist_data(args, test_data, cortical_result, dist_results):
    cong_embed_dists = dist_results['cong_dist_results']['cong_embed_dists']
    incong_embed_dists = dist_results['incong_dist_results']['incong_embed_dists']
    cong_hidd_dists = dist_results['cong_dist_results']['cong_hidd_dists']
    incong_hidd_dists = dist_results['incong_dist_results']['incong_hidd_dists']
    dist_c_inc_results = {'cong_embed_dist': cong_embed_dists, 'incong_embed_dist': incong_embed_dists, 'cong_hidd_dist': cong_hidd_dists, 'incong_hidd_dist': incong_hidd_dists}
    return dist_c_inc_results