def get_ngrams(D):
    """
    Returns all ngrams (aka a token containing a dollar sign ($)) from a set of topics or documents
    :param topics:
    :return:
    """
    ngrams = set()
    for d in D:
        for w in d:
            if '$' in w:
                ngrams.add(w)
    return list(ngrams)