def test_random_crop_and_resize_06():
    """
    Test RandomCropAndResize with c_transforms: invalid values for scale,
    expected to raise ValueError
    """
    logger.info('test_random_crop_and_resize_05_c')
    data = ds.TFRecordDataset(DATA_DIR, SCHEMA_DIR, columns_list=['image'], shuffle=False)
    decode_op = c_vision.Decode()
    try:
        random_crop_and_resize_op = c_vision.RandomResizedCrop((256, 512), scale='', ratio=(1, 0.5))
        data = data.map(input_columns=['image'], operations=decode_op)
        data.map(input_columns=['image'], operations=random_crop_and_resize_op)
    except TypeError as e:
        logger.info('Got an exception in DE: {}'.format(str(e)))
        assert 'Argument scale with value "" is not of type (<class \'tuple\'>,)' in str(e)
    try:
        random_crop_and_resize_op = c_vision.RandomResizedCrop((256, 512), scale=(1, '2'), ratio=(1, 0.5))
        data = data.map(input_columns=['image'], operations=decode_op)
        data.map(input_columns=['image'], operations=random_crop_and_resize_op)
    except TypeError as e:
        logger.info('Got an exception in DE: {}'.format(str(e)))
        assert "Argument scale[1] with value 2 is not of type (<class 'float'>, <class 'int'>)." in str(e)