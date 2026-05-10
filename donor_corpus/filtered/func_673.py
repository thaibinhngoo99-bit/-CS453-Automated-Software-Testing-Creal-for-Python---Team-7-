def is_rhyme(word1, word2, k):
    """
    Returns True if the last k letters of the two words are the same (case sensitive).
    Automatically returns False if either word contains less than k letters.
    """
    if k == 0:
        return False
    if len(word1) < k or len(word2) < k:
        return False
    rev_word1 = word1[::-1]
    rev_word2 = word2[::-1]
    return rev_word1[:k] == rev_word2[:k]