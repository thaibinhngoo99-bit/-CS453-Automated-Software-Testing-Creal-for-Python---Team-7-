def get_dataset_ngrams(docs, min_freq=1000, sw=None, extra_bigrams=None, extra_ngrams=None):
    if not sw:
        sw = stopwords.words('english')
        sw_pp = get_pp_pipeline(remove_stopwords=False)
        sw = sw_pp.clean_document(sw)
    full_text = []
    for doc in docs:
        full_text.extend(doc)
    frequent_bigrams = get_frequent_ngrams(full_text, 2, sw, min_freq)
    if extra_bigrams:
        frequent_bigrams.extend(extra_bigrams)
    bigrammized_text = ngrammize_text(full_text, frequent_bigrams)
    frequent_ngrams = get_frequent_ngrams(bigrammized_text, 2, sw, min_freq)
    if extra_ngrams:
        frequent_ngrams.extend(extra_ngrams)
    return (frequent_bigrams, frequent_ngrams)