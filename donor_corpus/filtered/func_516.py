def test_random_crop_and_resize_05_py():
    """
    Test RandomCropAndResize with py_transforms: invalid range of ratio (max<min),
    expected to raise ValueError
    """
    logger.info('test_random_crop_and_resize_05_py')
    data = ds.TFRecordDataset(DATA_DIR, SCHEMA_DIR, columns_list=['image'], shuffle=False)
    try:
        transforms = [py_vision.Decode(), py_vision.RandomResizedCrop((256, 512), (1, 1), (1, 0.5)), py_vision.ToTensor()]
        transform = mindspore.dataset.transforms.py_transforms.Compose(transforms)
        data = data.map(input_columns=['image'], operations=transform)
    except ValueError as e:
        logger.info('Got an exception in DE: {}'.format(str(e)))
        assert 'Input is not within the required interval of (0 to 16777216).' in str(e)