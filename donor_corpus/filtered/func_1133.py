def common_processing(df):
    df['tschq12'] = df['tschq12'].apply(lambda x: x / 100)
    df['tschq16'] = df['tschq16'].apply(lambda x: x / 100)
    df['tschq17'] = df['tschq17'].apply(lambda x: x / 100)
    df['tschq04'] = df.apply(smf.create_cols_family_hist, axis=1)
    return df