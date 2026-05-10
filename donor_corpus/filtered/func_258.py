def crossvalidate(edges, nonedges):
    random.shuffle(edges)
    random.shuffle(nonedges)
    train_edge_len, train_nonedge_len = (len(edges) * 7 // 10, len(nonedges) * 7 // 10)
    cross_edge_len, cross_nonedge_len = (len(edges) - train_edge_len, len(nonedges) - train_nonedge_len)
    X_train = normalize(nonedges[:train_nonedge_len] + edges[:train_edge_len])
    y_train = [0] * train_nonedge_len + [1] * train_edge_len
    X_cross = normalize(nonedges[train_nonedge_len:] + edges[train_edge_len:])
    y_cross = [0] * cross_nonedge_len + [1] * cross_edge_len
    clf = svm.SVC(gamma=0.001, C=100.0)
    clf.fit(X_train, y_train)
    print('prediction: {}'.format(list(clf.predict(X_cross))))
    print('actuallity: {}'.format(y_cross))
    print(clf.score(X_cross, y_cross))