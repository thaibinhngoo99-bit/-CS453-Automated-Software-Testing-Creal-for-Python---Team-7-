def test_random_crop_and_resize_02():
    """
    Test RandomCropAndResize with md5 check:Image interpolation mode is Inter.NEAREST,
    expected to pass
    """
    logger.info('test_random_crop_and_resize_02')
    original_seed = config_get_set_seed(0)
    original_num_parallel_workers = config_get_set_num_parallel_workers(1)
    data1 = ds.TFRecordDataset(DATA_DIR, SCHEMA_DIR, columns_list=['image'], shuffle=False)
    decode_op = c_vision.Decode()
    random_crop_and_resize_op = c_vision.RandomResizedCrop((256, 512), interpolation=mode.Inter.NEAREST)
    data1 = data1.map(input_columns=['image'], operations=decode_op)
    data1 = data1.map(input_columns=['image'], operations=random_crop_and_resize_op)
    data2 = ds.TFRecordDataset(DATA_DIR, SCHEMA_DIR, columns_list=['image'], shuffle=False)
    transforms = [py_vision.Decode(), py_vision.RandomResizedCrop((256, 512), interpolation=mode.Inter.NEAREST), py_vision.ToTensor()]
    transform = mindspore.dataset.transforms.py_transforms.Compose(transforms)
    data2 = data2.map(input_columns=['image'], operations=transform)
    filename1 = 'random_crop_and_resize_02_c_result.npz'
    filename2 = 'random_crop_and_resize_02_py_result.npz'
    save_and_check_md5(data1, filename1, generate_golden=GENERATE_GOLDEN)
    save_and_check_md5(data2, filename2, generate_golden=GENERATE_GOLDEN)
    ds.config.set_seed(original_seed)
    ds.config.set_num_parallel_workers(original_num_parallel_workers)