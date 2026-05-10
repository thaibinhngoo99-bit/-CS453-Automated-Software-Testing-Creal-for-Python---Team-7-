def initial_processing():
    tschq = pd.read_pickle(properties.data_location + '/input_pckl/' + '3_q.pckl')

    def filter_age(x):
        if isinstance(x, int):
            return tschq['tschq05'].value_counts().head(1).index[0]
        else:
            return x
    tschq['tschq05'] = tschq['tschq05'].apply(filter_age)
    tschq.drop(['questionnaire_id', 'created_at'], axis=1, inplace=True)
    hq = pd.read_pickle('data/input_pckl/4_q.pckl')
    hq.isna().sum(axis=0)
    hq.drop(['hq05', 'hq06'], axis=1, inplace=True)
    hq_df = hq.set_index('user_id')
    df = tschq.join(hq_df.iloc[:, 2:], on='user_id')
    drop_cols = ['tschq01', 'tschq25', 'tschq07-2', 'tschq13', 'tschq04-1', 'tschq04-2']
    df['tschq12'] = df['tschq12'].apply(lambda x: x / 100)
    df['tschq16'] = df['tschq16'].apply(lambda x: x / 100)
    df['tschq17'] = df['tschq17'].apply(lambda x: x / 100)
    df['tschq04'] = df.apply(smf.create_cols_family_hist, axis=1)
    df.drop(drop_cols, axis=1, inplace=True)
    categorical_feature_mask = df.iloc[:, 1:].infer_objects().dtypes == object
    other_feature_mask = df.iloc[:, 1:].infer_objects().dtypes != object
    categorical_cols = df.iloc[:, 1:].columns[categorical_feature_mask].tolist()
    num_cols = df.iloc[:, 1:].columns[other_feature_mask].tolist()
    cat_idx = [df.iloc[:, 1:].columns.get_loc(val) for val in categorical_cols]
    num_idx = [df.iloc[:, 1:].columns.get_loc(val) for val in num_cols]
    return (cat_idx, num_idx, df)