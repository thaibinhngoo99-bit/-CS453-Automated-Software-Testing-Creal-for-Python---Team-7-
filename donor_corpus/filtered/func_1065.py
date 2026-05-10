def concatString(path):
    corpus = ''
    with open(path, 'r', encoding='UTF-8') as f:
        for line in f.readlines():
            corpus += line
    return corpus