def get_pred_ref_points(user_id, ndays, method='mean'):
    test_user_ts = tsg_data.get_usr_mday_ts_predict(user_id)
    user_ts_idx = test_user_ts[:, 1]
    user_distress = test_user_ts[:, 3]
    prediction_at = round(len(user_ts_idx) * 0.8)
    y_labels = user_distress[prediction_at:prediction_at + ndays].tolist()
    prediction_at_list = user_ts_idx[prediction_at:prediction_at + ndays].tolist()
    return (y_labels, prediction_at_list)