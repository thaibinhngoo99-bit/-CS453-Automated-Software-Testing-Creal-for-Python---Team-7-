def one_hot_encode(token_lists, n_chars):
    output = np.zeros((len(token_lists), len(token_lists[0]), n_chars))
    for i, token_list in enumerate(token_lists):
        for j, token in enumerate(token_list):
            output[i, j, int(token)] = 1
    return output