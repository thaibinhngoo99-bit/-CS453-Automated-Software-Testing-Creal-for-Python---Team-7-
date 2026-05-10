def test_random_crop_and_resize_04_c():
    """
    Test RandomCropAndResize with c_tranforms: invalid range of scale (max<min),
    expected to raise ValueError
    """
    logger.info('test_random_crop_and_resize_04_c')
    data = ds.TFRecordDataset(DATA_DIR, SCHEMA_DIR, columns_list=['image'], shuffle=False)
    decode_op = c_vision.Decode()
    try:
        random_crop_and_resize_op = c_vision.RandomResizedCrop((256, 512), (1, 0.5), (0.5, 0.5))
        data = data.map(input_columns=['image'], operations=decode_op)
        data = data.map(input_columns=['image'], operations=random_crop_and_resize_op)
    except ValueError as e:
        logger.info('Got an exception in DE: {}'.format(str(e)))
        assert 'Input is not within the required interval of (0 to 16777216).' in str(e)