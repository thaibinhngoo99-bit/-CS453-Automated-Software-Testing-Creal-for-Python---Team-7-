def int_to_smile(array, indices_token, pad_char):
    """ 
    From an array of int, return a list of 
    molecules in string smile format
    Note: remove the padding char
    """
    all_mols = []
    for seq in array:
        new_mol = [indices_token[str(int(x))] for x in seq]
        all_mols.append(''.join(new_mol).replace(pad_char, ''))
    return all_mols