def compute_linear_regression(test_nn, encoded_data, pred_list, method='mean'):
    from sklearn.linear_model import LinearRegression
    preds = list()
    for point in pred_list:
        attr_list = list()
        intercepts_list = list()
        coeff_list = list()
        for nn in test_nn:
            u_id = encoded_data['user_id'].iloc[nn]
            user_ts = tsg_data.get_m_day_ts_enumerate(int(11))
            diff_arr = np.abs(np.subtract(point, user_ts[:, 1]))
            diff_near_idx = np.where(diff_arr == diff_arr.min())
            print(diff_near_idx)
            usr_vals = np.array([user_ts[n_id] for n_id in diff_near_idx[0]])
            if len(usr_vals) > 1:
                value = usr_vals.mean(axis=0)
                print('vavg' + str(value))
            else:
                value = usr_vals[0]
                print('v' + str(value))
            attr_list.append(value)
            df = pd.DataFrame(user_ts)
            df.columns = ['day', 'day_session_id', 's02', 's03', 's04', 's05', 's06', 's07']
            reg_model = LinearRegression(normalize=True)
            user_x = df[['day_session_id', 's04', 's05', 's06']].to_numpy()
            user_s03 = df[['s03']].to_numpy().ravel()
            reg_model.fit(user_x, user_s03)
            intercepts_list.append(reg_model.intercept_)
            coeff_list.append(reg_model.coef_)
        numpy_attr_list = np.array(attr_list)
        print(numpy_attr_list)
        avg_np_attr_list = numpy_attr_list[:, 4:].mean(axis=0)
        print(avg_np_attr_list)
        numpy_coeff_list = np.array(coeff_list)
        print(numpy_coeff_list)
        print(numpy_coeff_list.mean(axis=0))
        y = np.multiply(numpy_coeff_list[:, 0].mean(), point) + np.multiply(numpy_coeff_list[:, 1].mean(), avg_np_attr_list[0]) + np.multiply(numpy_coeff_list[:, 2].mean(), avg_np_attr_list[1]) + np.multiply(numpy_coeff_list[:, 3].mean(), avg_np_attr_list[2]) + np.asarray(intercepts_list).mean()
        preds.append(y)
    print(preds)
    return preds