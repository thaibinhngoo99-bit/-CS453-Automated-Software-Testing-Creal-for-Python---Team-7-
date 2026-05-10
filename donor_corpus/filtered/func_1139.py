def create_y_labels(test_data, prediction_at, method='mean'):
    y_test = list()
    for i in range(0, len(test_data)):
        test_ts_test1 = tsg_data.get_usr_mday_ts_predict(int(test_data.iloc[i]['user_id']))
        if len(test_ts_test1) >= prediction_at:
            y_test.append(test_ts_test1[prediction_at - 1][2])
        elif len(test_ts_test1) < prediction_at:
            y_test.append(test_ts_test1[len(test_ts_test1) - 1][2])
    return y_test