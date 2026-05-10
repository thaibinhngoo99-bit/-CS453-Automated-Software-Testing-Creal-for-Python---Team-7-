def rename_fmapm(bids_base, basename):
    """
    Rename magnitude fieldmap file to BIDS specification
    """
    files = dict()
    for ext in ['nii.gz', 'json']:
        for echo in [1, 2]:
            fname = '{0}_e{1}.{2}'.format(basename, echo, ext)
            src = os.path.join(bids_base, 'fmap', fname)
            if os.path.exists(src):
                dst = src.replace('magnitude_e{0}'.format(echo), 'magnitude{0}'.format(echo))
                logger.debug('renaming %s to %s', src, dst)
                os.rename(src, dst)
                files[ext] = dst
    return files