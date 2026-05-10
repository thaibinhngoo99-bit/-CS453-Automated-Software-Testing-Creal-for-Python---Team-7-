def get_frequent_ngrams(text, n, stopword_list, threshold):
    bigrams = ngrams(text, n)
    bigram_freq = Counter(bigrams)
    frequent_bigrams = []
    for bigram, freq in bigram_freq.most_common():
        if not or_list([i in stopword_list for i in bigram]):
            if freq > threshold:
                frequent_bigrams.append('{}${}'.format(bigram[0], bigram[1]))
            else:
                break
    return frequent_bigrams