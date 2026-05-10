def train(edges, nonedges):
    clf = svm.SVC(gamma=0.001, C=100.0)
    X = normalize(nonedges + edges)
    y = [0] * len(nonedges) + [1] * len(edges)
    clf.fit(X, y)
    return clf