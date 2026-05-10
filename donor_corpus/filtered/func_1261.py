def featureSelection_variance(X, thrd):
    sel = VarianceThreshold(threshold=thrd)
    X_selected = sel.fit_transform(X)
    mask = sel.get_support()
    return (X_selected, mask)