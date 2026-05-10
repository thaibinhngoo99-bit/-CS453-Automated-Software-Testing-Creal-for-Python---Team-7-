def ngrammize_text(text, ngrams):
    bigrammized_text = []
    i = 0
    while i < len(text):
        term = text[i]
        if i == len(text) - 1:
            bigrammized_text.append(term)
        else:
            next_term = text[i + 1]
            test_bigram = '{}${}'.format(term, next_term)
            if test_bigram in ngrams:
                bigrammized_text.append(test_bigram)
                i += 1
            else:
                bigrammized_text.append(term)
        i += 1
    return bigrammized_text