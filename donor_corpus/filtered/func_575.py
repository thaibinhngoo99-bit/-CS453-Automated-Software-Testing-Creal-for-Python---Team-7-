def calc_ratio(args, test_data, cortical_result, dist_results):
    cong_embed_dists = dist_results['cong_dist_results']['cong_embed_dists']
    incong_embed_dists = dist_results['incong_dist_results']['incong_embed_dists']
    avg_cong_embed = np.mean(cong_embed_dists)
    avg_incong_embed = np.mean(incong_embed_dists)
    ratio_embed = avg_cong_embed / avg_incong_embed
    cong_hidd_dists = dist_results['cong_dist_results']['cong_hidd_dists']
    incong_hidd_dists = dist_results['incong_dist_results']['incong_hidd_dists']
    avg_cong_hidd = np.mean(cong_hidd_dists, axis=0)
    avg_incong_hidd = np.mean(incong_hidd_dists, axis=0)
    ratio_hidd = avg_incong_hidd / avg_cong_hidd
    ratio_results = {'ratio_embed': ratio_embed, 'ratio_hidd': ratio_hidd, 'avg_cong_hidd': avg_cong_hidd, 'avg_incong_hidd': avg_incong_hidd}
    return ratio_results