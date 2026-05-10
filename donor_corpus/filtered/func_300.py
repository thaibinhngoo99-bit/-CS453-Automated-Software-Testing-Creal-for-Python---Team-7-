def convert_by_vocab(vocab, items):
    """Converts a sequence of [tokens|ids] using the vocab."""
    output = []
    for i, item in enumerate(items):
        output.append(vocab[item])
    return output