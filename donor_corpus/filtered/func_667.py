def test_load_collection_arguments(requests_mock):
    conn = Connection(API_URL)
    requests_mock.get(API_URL, json={'version': '0.4.0'})
    requests_mock.get(API_URL + 'collections/FOO', json={'properties': {'eo:bands': [{'name': 'red'}, {'name': 'green'}, {'name': 'blue'}]}})
    spatial_extent = {'west': 1, 'south': 2, 'east': 3, 'north': 4}
    temporal_extent = ['2019-01-01', '2019-01-22']
    im = conn.load_collection('FOO', spatial_extent=spatial_extent, temporal_extent=temporal_extent, bands=['red', 'green'])
    node = im.graph[im.node_id]
    assert node['process_id'] == 'load_collection'
    assert node['arguments'] == {'id': 'FOO', 'spatial_extent': spatial_extent, 'temporal_extent': temporal_extent, 'bands': ['red', 'green']}