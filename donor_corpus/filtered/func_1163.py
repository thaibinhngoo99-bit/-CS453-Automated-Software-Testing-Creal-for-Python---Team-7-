def test_KMLCaching_not_possible():
    import os.path
    import sys

    class Mock(object):
        pass
    mock_stderr = Mock()
    buffer = []

    def mock_write(error_message):
        buffer.append(error_message)
    mock_stderr.write = mock_write
    with s3gis_tests.Change(os.path, {'exists': lambda *a, **kw: False}):
        with s3gis_tests.Change(sys, {'stderr': mock_stderr}):
            with s3gis_tests.Change(current.session.s3, {'debug': False}):
                kml_layer = s3gis.KMLLayer(s3gis.GIS())
                js = kml_layer.as_javascript()
                assert session.error.startswith('GIS: KML layers cannot be cached: ')
                assert 'GIS: KML layers cannot be cached:' in buffer[0]