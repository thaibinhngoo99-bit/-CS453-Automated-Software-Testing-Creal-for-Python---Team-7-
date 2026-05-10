def sample(model, temp, start_char, end_char, max_len, indices_token, token_indices):
    n_chars = len(indices_token)
    seed_token = [token_indices[start_char]]
    generated = indices_token[str(seed_token[0])]
    while generated[-1] != end_char and len(generated) < max_len:
        x_seed = one_hot_encode([seed_token], n_chars)
        full_preds = model.predict(x_seed, verbose=0)[0]
        logits = full_preds[-1]
        probas, next_char_ind = get_token_proba(logits, temp)
        next_char = indices_token[str(next_char_ind)]
        generated += next_char
        seed_token += [next_char_ind]
    return generated