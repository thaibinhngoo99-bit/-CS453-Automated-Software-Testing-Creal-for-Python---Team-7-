def get_token_proba(preds, temp):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temp
    exp_preds = np.exp(preds)
    probas = exp_preds / np.sum(exp_preds)
    char_ind = np.argmax(np.random.multinomial(1, probas, 1))
    return (probas, char_ind)