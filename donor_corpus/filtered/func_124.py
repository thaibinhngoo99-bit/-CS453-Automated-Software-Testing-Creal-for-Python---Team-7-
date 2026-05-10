def benjamini_hochberg_test(df_pvalues, hypotheses_independent, fdr_level):
    """
    This is an implementation of the benjamini hochberg procedure that calculates which of the hypotheses belonging
    to the different p-Values from df_p to reject. While doing so, this test controls the false discovery rate,
    which is the ratio of false rejections by all rejections:

    .. math::

        FDR = \\mathbb{E} \\left [ \\frac{ |\\text{false rejections}| }{ |\\text{all rejections}|} \\right]


    References
    ----------

    .. [1] Benjamini, Yoav and Yekutieli, Daniel (2001).
        The control of the false discovery rate in multiple testing under dependency.
        Annals of statistics, 1165--1188


    :param df_pvalues: This DataFrame should contain the p_values of the different hypotheses in a column named
                       "p_values".
    :type df_pvalues: pandas.DataFrame

    :param hypotheses_independent: Can the significance of the features be assumed to be independent?
                                   Normally, this should be set to False as the features are never
                                   independent (e.g. mean and median)
    :type hypotheses_independent: bool

    :param fdr_level: The FDR level that should be respected, this is the theoretical expected percentage of irrelevant
                      features among all created features.
    :type fdr_level: float

    :return: The same DataFrame as the input, but with an added boolean column "rejected".
    :rtype: pandas.DataFrame
    """
    df_pvalues = df_pvalues.sort_values(by='p_value')
    m = len(df_pvalues)
    K = list(range(1, m + 1))
    if hypotheses_independent:
        C = [1] * m
    else:
        C = [sum([1.0 / i for i in range(1, k + 1)]) for k in K]
    T = [fdr_level * k / m * 1.0 / c for k, c in zip(K, C)]
    try:
        k_max = list(df_pvalues.p_value <= T).index(False)
    except ValueError:
        k_max = m
    df_pvalues['rejected'] = [True] * k_max + [False] * (m - k_max)
    return df_pvalues