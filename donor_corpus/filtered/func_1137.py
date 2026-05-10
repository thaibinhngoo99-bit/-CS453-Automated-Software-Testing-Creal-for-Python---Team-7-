def compute(test_nn, encoded_data, pred_list, method='mean', dist_nn=None, wt_dist=False):
    from sklearn.linear_model import LinearRegression
    preds = list()
    for point in pred_list:
        nn_preds = list()
        intercepts_list = list()
        coeff_list = list()
        for nn in test_nn:
            u_id = encoded_data['user_id'].iloc[nn]
            user_ts = tsg_data.get_usr_mday_ts_predict(int(u_id))
            diff_arr = np.abs(np.subtract(point, user_ts[:, 1]))
            diff_near_idx = np.where(diff_arr == diff_arr.min())
            print('minimum to the time point is at -- ', diff_near_idx)
            usr_idx = diff_near_idx[0][0]
            user_ts_p = user_ts[:usr_idx]
            user_ts_df = pd.DataFrame(user_ts_p, columns=['day', 'day_sess_index', 's02', 's03', 's04', 's05', 's06', 's07'])
            X = user_ts_df[['day_sess_index']]
            y = user_ts_df[['s03']]
            reg_fit = LinearRegression(normalize=True)
            reg_fit.fit(X, y)
            if wt_dist:
                nn_pred = reg_fit.predict(np.asarray(point).reshape(1, -1))
                nn_preds.append(nn_pred[0][0])
            else:
                intercepts_list.append(reg_fit.intercept_)
                coeff_list.append(reg_fit.coef_)
        if wt_dist:
            print('Predicting the value of s03 for the user by a weighted average weighted by distance')
            preds.append(weighted_distance_prediction(nn_preds, dist_nn))
        else:
            print('Predicting the value of s3 over the averaged slope and intercepts of observations of the neighbors')
            print('The equation to estimate s03 for the user is {}'.format(''.join(str(np.asarray(coeff_list).mean())) + '* time_index + ' + str(np.asarray(intercepts_list).mean())))
            y = np.multiply(np.asarray(coeff_list).mean(), point) + np.asarray(intercepts_list).mean()
            preds.append(y)
    return preds