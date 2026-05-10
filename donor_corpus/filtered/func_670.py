def limit(img, std_hash, count):
    """
    Determine whether image should be removed from image dictionary in main.py
        img: (ndarray) image file
        std_hash: (array) wavelet hash of comparison standard
        count: (int) global count of images similar to comparison standard
    """
    cmp_hash = calc_hash(img)
    diff = compare(std_hash, cmp_hash)
    if diff <= DIFF_THRES:
        if count >= LIMIT:
            return 'remove'
    else:
        return 'update_std'
    return 'continue'