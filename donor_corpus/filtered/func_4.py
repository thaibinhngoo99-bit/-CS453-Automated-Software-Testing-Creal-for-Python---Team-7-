def multiplyMatrices(pieces, field, norm=True):
    pieces = pieces.astype(np.float64)
    field = field.astype(np.float64)
    pieces_sum = np.zeros(piece_shape)
    field_sum = np.zeros(field[0].shape)
    for i in range(0, len(pieces)):
        pieces[i] = np.multiply(pieces[i], i + 1)
        if norm:
            pieces[i] /= NUM_COLORS
        pieces_sum += pieces[i]
    for i in range(0, len(field)):
        field[i] = np.multiply(field[i], i + 1)
        if norm:
            field[i] /= NUM_COLORS
        field_sum += field[i]
    return (pieces_sum, field_sum)