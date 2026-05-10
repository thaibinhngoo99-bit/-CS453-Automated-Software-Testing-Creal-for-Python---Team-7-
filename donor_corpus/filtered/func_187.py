def round_mask(filename):
    mask, affine, spacing, header = utils.load_nifty(filename)
    mask = np.rint(mask)
    mask = mask.astype(int)
    utils.save_nifty(filename, mask, affine, spacing, header)