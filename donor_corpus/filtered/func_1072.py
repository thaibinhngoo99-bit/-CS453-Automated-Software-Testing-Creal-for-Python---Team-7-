def lamost_filepath(planid, mjd, spid, fiberid, dirpath='', extname='.fits'):
    """ generate file path of a LAMOST spectrum

    Parameters
    ----------
    planid: string
        planid

    mjd: 5-digit integer
        mjd (use lmjd rather than mjd for DR3 and after!)

    spid: 2-digit integer
        spid, the number of the spectrogragh

    fiberid: 3-digit integer
        fiberid

    dirpath: string
        the root directory for storing spectra.

    Returns
    --------
    filepath: string
        the path of root dir of directory (prefix).
        if un-specified, return file name.

    """
    if np.isscalar(planid):
        planid = planid.strip()
    else:
        planid = [_.strip() for _ in planid]
    if dirpath == '' or dirpath is None:
        if np.isscalar(mjd):
            return 'spec-%05d-%s_sp%02d-%03d%s' % (mjd, planid, spid, fiberid, extname)
        else:
            return np.array(['spec-%05d-%s_sp%02d-%03d%s' % (mjd[i], planid[i], spid[i], fiberid[i], extname) for i in range(len(mjd))])
    else:
        if not dirpath[-1] == os.path.sep:
            dirpath += os.path.sep
        if np.isscalar(mjd):
            return '%s%s%sspec-%05d-%s_sp%02d-%03d%s' % (dirpath, planid, os.path.sep, mjd, planid, spid, fiberid, extname)
        else:
            return np.array(['%s%s%sspec-%05d-%s_sp%02d-%03d%s' % (dirpath, planid[i], os.path.sep, mjd[i], planid[i], spid[i], fiberid[i], extname) for i in range(len(mjd))])