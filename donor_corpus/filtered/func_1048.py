def extract_info_from_setup():
    with mock.patch.object(setuptools, 'setup') as mock_setup:
        import data_collector.downloaded_packages.setup
    args, kwargs = mock_setup.call_args
    print(kwargs)