def merge_labels(load_mask, save_mask, load_label_table):
    mask, affine, spacing, header = utils.load_nifty(load_mask)
    mask = mask.astype(int)
    ggo, cons, pe = get_labels(load_label_table)
    for label in tqdm(np.concatenate((ggo, cons, pe), axis=0), disable=True):
        mask[mask == label] = -label
    for label in tqdm(ggo, disable=True):
        mask[mask == -label] = 1
    for label in tqdm(cons, disable=True):
        mask[mask == -label] = 2
    for label in tqdm(pe, disable=True):
        mask[mask == -label] = 3
    mask = np.rint(mask)
    mask = mask.astype(int)
    utils.save_nifty(save_mask, mask, affine, spacing, header)