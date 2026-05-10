def search_picture(clf, image_name):
    image = Image.open(image_name).convert('1')
    x, y = image.size
    image = image.resize((x, 280), Image.ANTIALIAS)
    w, h = image.size
    columns = [get_column(image, i) for i in range(25)]
    datas = []
    for i in range(25, w):
        columns = columns[1:] + [get_column(image, i)]
        data = [columns[i][j] for j in range(len(columns[0])) for i in range(len(columns))]
        datas.append(data)
    datas = normalize(datas)
    matches = [[i] for i, m in enumerate(clf.predict(datas)) if m == 1]
    if len(matches) == 0:
        return ([], matches)
    clst = cluster.DBSCAN(eps=20, min_samples=1)
    clst.fit(matches)
    trimmed = [idx for idx in clst.components_ if idx > w // 6 and idx < w * 5 // 6]
    clst = cluster.KMeans(3, init='k-means++')
    clst.fit(trimmed)
    seps = list(sorted([int(v[0]) + 25 // 2 for v in clst.cluster_centers_]))
    final_seps = []
    for start, end in zip(seps, seps[1:]):
        if end - start > w // 6:
            final_seps.append(start)
    final_seps.append(seps[-1])
    return (final_seps, matches)