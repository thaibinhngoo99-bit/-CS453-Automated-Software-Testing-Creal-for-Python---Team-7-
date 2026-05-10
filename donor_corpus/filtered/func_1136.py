def weighted_distance_prediction(p_preds, distance):
    inv_dist = np.divide(1, distance)
    s03_pred = np.sum(np.multiply(p_preds, inv_dist)) / np.sum(inv_dist)
    return s03_pred