def get_scaled_imgs(df):
    imgs = []
    for i, row in df.iterrows():
        band_1 = np.array(row['band_1'])
        band_2 = np.array(row['band_2'])
        band_1 = band_1.reshape(75, 75)
        band_2 = band_2.reshape(75, 75)
        a = (band_1 - band_1.mean()) / (band_1.max() - band_1.min())
        b = (band_2 - band_2.mean()) / (band_2.max() - band_2.min())
        imgs.append(np.dstack((a, b)))
    return np.array(imgs)