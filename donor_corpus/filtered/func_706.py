def _load_tcc(f_tcc, msk):
    from gio import geo_raster_ex as gx
    from gio import config
    import numpy as np
    _bnd = gx.read_block(f_tcc, msk)
    if _bnd is None:
        return None
    _dat = np.zeros(msk.data.shape, dtype=np.uint8)
    _m_tcc = config.getfloat('conf', 'min_tcc')
    _idx = _bnd.data >= _m_tcc
    _dat[_idx] = 100
    _idx = _bnd.data > 100
    _dat[_idx] = _bnd.data[_idx]
    return msk.from_grid(_dat, nodata=255)