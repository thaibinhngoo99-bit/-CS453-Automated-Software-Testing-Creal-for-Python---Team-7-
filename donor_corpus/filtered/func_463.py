def my_test_suite():
    """From http://stackoverflow.com/questions/17001010/.

    """
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite