def plot_iris_knn():
    iris = datasets.load_iris()
    X = iris.data[:, :2]
    y = iris.target
    knn = neighbors.KNeighborsClassifier(n_neighbors=3)
    knn.fit(X, y)
    x_min, x_max = (X[:, 0].min() - 0.1, X[:, 0].max() + 0.1)
    y_min, y_max = (X[:, 1].min() - 0.1, X[:, 1].max() + 0.1)
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
    Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    pl.figure()
    pl.pcolormesh(xx, yy, Z, cmap=cmap_light)
    pl.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold)
    pl.xlabel('sepal length (cm)')
    pl.ylabel('sepal width (cm)')
    pl.axis('tight')