def _test_lamost_filepath():
    """test function **lamost_filepath**
    """
    print(lamost_filepath('GAC_061N46_V3', 55939, 7, 78))
    print(lamost_filepath('GAC_061N46_V3', 55939, 7, 78, '/'))
    print(lamost_filepath('GAC_061N46_V3', 55939, 7, 78, '/pool'))
    print(lamost_filepath('GAC_061N46_V3', 55939, 7, 78, '/pool/'))