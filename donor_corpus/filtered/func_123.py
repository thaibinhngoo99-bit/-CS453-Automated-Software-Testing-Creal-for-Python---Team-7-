def check_fs_sig_bh(X, y, n_processes=defaults.N_PROCESSES, chunksize=defaults.CHUNKSIZE, fdr_level=defaults.FDR_LEVEL, hypotheses_independent=defaults.HYPOTHESES_INDEPENDENT, test_for_binary_target_real_feature=defaults.TEST_FOR_BINARY_TARGET_REAL_FEATURE):
    """
    The wrapper function that calls the significance test functions in this package.
    In total, for each feature from the input pandas.DataFrame an univariate feature significance test is conducted.
    Those tests generate p values that are then evaluated by the Benjamini Hochberg procedure to decide which features
    to keep and which to delete.

    We are testing
    
        :math:`H_0` = the Feature is not relevant and can not be added

    against

        :math:`H_1` = the Feature is relevant and should be kept
   
    or in other words
 
        :math:`H_0` = Target and Feature are independent / the Feature has no influence on the target

        :math:`H_1` = Target and Feature are associated / dependent

    When the target is binary this becomes
    
        :math:`H_0 = \\left( F_{\\text{target}=1} = F_{\\text{target}=0} \\right)`

        :math:`H_1 = \\left( F_{\\text{target}=1} \\neq F_{\\text{target}=0} \\right)`
    
    Where :math:`F` is the distribution of the target.

    In the same way we can state the hypothesis when the feature is binary
    
        :math:`H_0 =  \\left( T_{\\text{feature}=1} = T_{\\text{feature}=0} \\right)`

        :math:`H_1 = \\left( T_{\\text{feature}=1} \\neq T_{\\text{feature}=0} \\right)`

    Here :math:`T` is the distribution of the target.

    TODO: And for real valued?

    :param X: The DataFrame containing all the features and the target
    :type X: pandas.DataFrame

    :param y: The target vector
    :type y: pandas.Series

    :param test_for_binary_target_real_feature: Which test to be used for binary target, real feature
    :type test_for_binary_target_real_feature: str

    :param fdr_level: The FDR level that should be respected, this is the theoretical expected percentage of irrelevant
                      features among all created features.
    :type fdr_level: float

    :param hypotheses_independent: Can the significance of the features be assumed to be independent?
                                   Normally, this should be set to False as the features are never
                                   independent (e.g. mean and median)
    :type hypotheses_independent: bool

    :param n_processes: Number of processes to use during the p-value calculation
    :type n_processes: int

    :param chunksize: Size of the chunks submitted to the worker processes
    :type chunksize: int

    :return: A pandas.DataFrame with each column of the input DataFrame X as index with information on the significance
            of this particular feature. The DataFrame has the columns
            "Feature",
            "type" (binary, real or const),
            "p_value" (the significance of this feature as a p-value, lower means more significant)
            "rejected" (if the Benjamini Hochberg procedure rejected this feature)
    :rtype: pandas.DataFrame

    """
    target_is_binary = len(set(y)) == 2
    y = y.astype(np.float)
    X = X.copy().loc[~(y == np.NaN), :]
    df_features = pd.DataFrame()
    df_features['Feature'] = list(set(X.columns))
    df_features = df_features.set_index('Feature', drop=False)
    df_features['rejected'] = np.nan
    df_features['type'] = np.nan
    df_features['p_value'] = np.nan
    pool = Pool(n_processes)
    f = partial(_calculate_p_value, y=y, target_is_binary=target_is_binary, test_for_binary_target_real_feature=test_for_binary_target_real_feature)
    results = pool.map(f, [X[feature] for feature in df_features['Feature']], chunksize=chunksize)
    p_values_of_features = pd.DataFrame(results)
    df_features.update(p_values_of_features)
    pool.close()
    pool.join()
    if 'const' in set(df_features.type):
        df_features_bh = benjamini_hochberg_test(df_features.loc[~(df_features.type == 'const')], hypotheses_independent, fdr_level)
        df_features = pd.concat([df_features_bh, df_features.loc[df_features.type == 'const']])
    else:
        df_features = benjamini_hochberg_test(df_features, hypotheses_independent, fdr_level)
    df_features['rejected'] = df_features['rejected'].astype('bool')
    if defaults.WRITE_SELECTION_REPORT:
        if not os.path.exists(defaults.RESULT_DIR):
            os.mkdir(defaults.RESULT_DIR)
        with open(os.path.join(defaults.RESULT_DIR, 'fs_bh_results.txt'), 'w') as file_out:
            file_out.write('Performed BH Test to control the false discovery rate(FDR); \nFDR-Level={0};Hypothesis independent={1}\n'.format(fdr_level, hypotheses_independent))
            df_features.to_csv(index=False, path_or_buf=file_out, sep=';', float_format='%.4f')
    return df_features