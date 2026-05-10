def extract_hidd_dist(dist_results):
    cong_hidd_dists = dist_results['cong_dist_results']['cong_hidd_dists']
    incong_hidd_dists = dist_results['incong_dist_results']['incong_hidd_dists']
    dist_result_hidd = {'cong_hidd_dists': cong_hidd_dists, 'incong_hidd_dists': incong_hidd_dists}
    return dist_result_hidd