def split_training(dense_table, metadata, design, training_column=None, num_random_test_examples=10, seed=None):
    if training_column is None:
        np.random.seed(seed)
        idx = np.random.random(design.shape[0])
        i = np.argsort(idx)[num_random_test_examples]
        threshold = idx[i]
        train_idx = ~(idx < threshold)
    else:
        train_idx = metadata.loc[design.index, training_column] == 'Train'
    trainX = design.loc[train_idx].values
    testX = design.loc[~train_idx].values
    trainY = dense_table.loc[train_idx].values
    testY = dense_table.loc[~train_idx].values
    return (trainX, testX, trainY, testY)