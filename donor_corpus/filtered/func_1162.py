def test_KMLLayer():
    current.session.s3.debug = True
    current.request.utcnow = datetime.datetime.now()
    s3gis_tests.layer_test(db, db.gis_layer_kml, dict(name='Test KML', description='Test KML layer', enabled=True, created_on=datetime.datetime.now(), modified_on=datetime.datetime.now(), url='test://test_KML'), 'S3.gis.layers_kml', [{'marker_height': 34, 'marker_image': u'gis_marker.image.marker_red.png', 'marker_width': 20, 'name': u'Test KML', 'url': u'/eden/default/download/gis_cache2.file.Test_20KML.kml'}], session=session, request=request)