def extract_hard_alignment(attn, src_sent, tgt_sent, pad, eos):
    tgt_valid = ((tgt_sent != pad) & (tgt_sent != eos)).nonzero().squeeze(dim=-1)
    src_invalid = ((src_sent == pad) | (src_sent == eos)).nonzero().squeeze(dim=-1)
    src_token_to_word = get_token_to_word_mapping(src_sent, [eos, pad])
    tgt_token_to_word = get_token_to_word_mapping(tgt_sent, [eos, pad])
    alignment = []
    if len(tgt_valid) != 0 and len(src_invalid) < len(src_sent):
        attn_valid = attn[tgt_valid]
        attn_valid[:, src_invalid] = float('-inf')
        _, src_indices = attn_valid.max(dim=1)
        for tgt_idx, src_idx in zip(tgt_valid, src_indices):
            alignment.append((src_token_to_word[src_idx.item()] - 1, tgt_token_to_word[tgt_idx.item()] - 1))
    return alignment