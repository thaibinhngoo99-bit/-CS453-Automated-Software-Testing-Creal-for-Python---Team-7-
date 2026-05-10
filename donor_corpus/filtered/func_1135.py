def compute_weighted_avg(n_idx, encoded_data, pred_at_list, method='mean', dist_nn=None, wt_flag=False):
    preds = list()
    for pval in pred_at_list:
        distress_list = list()
        for vals in n_idx:
            u_id = encoded_data['user_id'].iloc[vals]
            user_ts = tsg_data.get_usr_mday_ts_predict(int(u_id))
            print('{}, {} Values '.format(int(pval), int(u_id)))
            if len(user_ts) > int(pval):
                value = user_ts[int(pval), :][3]
            elif len(user_ts) <= int(pval):
                value = user_ts[len(user_ts) - 1, :][3]
            distress_list.append(value)
        if wt_flag:
            print('Calling by weighted distance prediction for distress')
            preds.append(weighted_distance_prediction(distress_list, dist_nn))
        else:
            print('Calling weighted average to predict distress')
            preds.append(weighted_average(distress_list))
    return preds