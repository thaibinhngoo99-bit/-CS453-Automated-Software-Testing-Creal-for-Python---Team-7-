def rename_fmapp(bids_base, basename):
    """
    Rename phase fieldmap file to BIDS specification
    """
    files = dict()
    for ext in ['nii.gz', 'json']:
        fname = '{0}_e2_ph.{1}'.format(basename, ext)
        src = os.path.join(bids_base, 'fmap', fname)
        if os.path.exists(src):
            dst = src.replace('phase_e2_ph', 'phase')
            logger.debug('renaming %s to %s', src, dst)
            os.rename(src, dst)
            files[ext] = dst
    return files