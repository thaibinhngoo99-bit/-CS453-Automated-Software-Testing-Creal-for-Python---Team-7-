def plot_roc_curve(y_test, y_pred_probas, proba_step=None):
    """
    Plot ROC curve with probabilities thresholds.
    
    Parameters
    ----------
    y_test : array-like
        true labels
    
    y_pred_probas : array-like
        predicted labels
    
    proba_step : int (optional) (default=None)
        if set, give the step for each probability display. If None, nothing is displayed.

    Examples
    --------
    
    >>> from dsbox.ml.visualization.metrics import plot_roc_curve
    >>> from sklearn import datasets
    >>> from sklearn.model_selection import train_test_split
    >>> from sklearn.ensemble import RandomForestClassifier
    
    >>> X, y = datasets.make_moons(noise=0.3, random_state=0)
    >>> X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5, random_state=0)
    
    >>> clf = RandomForestClassifier(n_estimators=10, random_state=42)
    >>> _ = clf.fit(X_train, y_train)
    >>> y_pred_probas = clf.predict_proba(X_test)
    
    >>> plot_roc_curve(y_test, y_pred_probas, proba_step=2)

    """
    fpr, tpr, thresholds = roc_curve(y_test, y_pred_probas[:, 1])
    auc_score = auc(fpr, tpr)
    plt.figure()
    lw = 1
    plt.plot(fpr, tpr, color='darkorange', lw=lw, marker='.')
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    if proba_step is not None:
        i = 0
        for x, y, txt in zip(fpr, tpr, thresholds):
            if i % proba_step == 0:
                plt.annotate(np.round(txt, 2), (x, y - 0.04), color='darkgray', fontsize=8)
            i += 1
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic (ROC) - AUC score: {}'.format(str(np.round(auc_score, 3))))
    plt.show()