def usage():
    _p = environ_mag.usage(True)
    _p.add_argument('-i', '--input', dest='input')
    _p.add_argument('-r', '--refer', dest='refer')
    _p.add_argument('--latest-tcc', dest='latest_tcc')
    _p.add_argument('-w', '--over-write', dest='over_write', type='bool')
    _p.add_argument('--min-tcc', dest='min_tcc', type=int, default=30)
    _p.add_argument('-m', '--min-patch', dest='min_patch', type=float, default=100 * 100)
    _p.add_argument('--test-tile', dest='test_tile')
    return _p