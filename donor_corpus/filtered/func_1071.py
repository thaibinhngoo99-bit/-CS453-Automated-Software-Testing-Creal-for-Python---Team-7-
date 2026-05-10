def predictSentences(index2word, unk_char, ini_char, ini_idx, model, test_pairs, print_every, batch_size, max_senten_len, max_context_size):
    model.eval()
    pairs_batches, num_batches = buildingPairsBatch(test_pairs, batch_size, shuffle=False)
    print('')
    print('num of batch:', num_batches)
    predict_sentences = []
    idx_batch = 0
    for contexts_tensor_batch, pad_matrix_batch in getTensorsContextPairsBatch(word2index, pairs_batches, max_context_size):
        predict_batch = model.predict(contexts_tensor_batch, index2word, pad_matrix_batch, ini_idx, sep_char='\t')
        predict_sentences.extend(predict_batch)
        if (idx_batch + 1) % print_every == 0:
            print('{} batches finished'.format(idx_batch + 1))
        idx_batch += 1
    predict_sentences = predict_sentences[0:len(test_pairs)]
    return predict_sentences