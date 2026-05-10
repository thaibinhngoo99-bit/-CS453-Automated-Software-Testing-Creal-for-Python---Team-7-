def normalize(X):
    global min_len
    min_len = min(min_len, min((len(x) for x in X)))
    return [x[:min_len] for x in X]