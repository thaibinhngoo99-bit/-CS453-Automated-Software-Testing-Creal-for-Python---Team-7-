def word_embedding_compression(word_embedding_module, d_model):
    """
    Compresses a given word_embedding_module (type torch.Embedding) into a module of d_model dimensionality.
    """
    word_embedding_matrix = word_embedding_module.weight
    assert word_embedding_matrix.shape[1] >= d_model, 'The desired word embedding dimensionality is greater than the teacher word embeddings. That is not compression! Make d_model smaller.'
    if word_embedding_matrix.shape[1] == d_model:
        return word_embedding_module
    pca = PCA(n_components=d_model)
    compressed_word_embedding_matrix = pca.fit_transform(word_embedding_matrix.detach().cpu().numpy())
    compressed_word_embedding_matrix = torch.from_numpy(compressed_word_embedding_matrix)
    word_embedding_module.weight = torch.nn.parameter.Parameter(compressed_word_embedding_matrix)
    return word_embedding_module