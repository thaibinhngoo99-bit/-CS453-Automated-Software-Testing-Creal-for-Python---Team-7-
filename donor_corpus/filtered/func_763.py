def replace_unk(hypo_str, src_str, alignment, align_dict, unk):
    from fairseq import tokenizer
    hypo_tokens = tokenizer.tokenize_line(hypo_str)
    src_tokens = tokenizer.tokenize_line(src_str) + ['<eos>']
    for i, ht in enumerate(hypo_tokens):
        if ht == unk:
            src_token = src_tokens[alignment[i]]
            hypo_tokens[i] = align_dict.get(src_token, src_token)
    return ' '.join(hypo_tokens)