def preProcess(word2index, test_contexts, unk_char, ini_char, max_senten_len, max_context_size):
    print('preprocessing...')
    filter_test_contexts = []
    for context in test_contexts:
        filter_context = [filteringSenten(word2index, senten, unk_char, ini_char) for senten in context]
        filter_test_contexts.append(filter_context)
    padded_test_pairs = []
    for context in filter_test_contexts:
        pad_list = [0] * len(context)
        if len(context) <= max_context_size:
            pad_list = [1] * (max_context_size - len(context)) + pad_list
            context = ['<unk>'] * (max_context_size - len(context)) + context
        else:
            pad_list = pad_list[-max_context_size:]
            context = context[-max_context_size:]
        padded_context = [paddingSenten(senten, max_senten_len) for senten in context]
        padded_test_pairs.append([padded_context, pad_list])
    return padded_test_pairs