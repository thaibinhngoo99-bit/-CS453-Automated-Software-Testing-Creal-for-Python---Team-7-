def splitData(dataset, test_user_ids):
    train_data = dataset[~dataset['user_id'].isin(test_user_ids)]
    test_data = dataset[dataset['user_id'].isin(test_user_ids)]
    return (train_data, test_data)