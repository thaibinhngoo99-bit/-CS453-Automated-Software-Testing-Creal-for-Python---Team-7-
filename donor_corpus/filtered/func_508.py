def test_random_crop_and_resize_op_c(plot=False):
    """
    Test RandomCropAndResize op in c transforms
    """
    logger.info('test_random_crop_and_resize_op_c')
    data1 = ds.TFRecordDataset(DATA_DIR, SCHEMA_DIR, columns_list=['image'], shuffle=False)
    decode_op = c_vision.Decode()
    random_crop_and_resize_op = c_vision.RandomResizedCrop((256, 512), (2, 2), (1, 3))
    data1 = data1.map(input_columns=['image'], operations=decode_op)
    data1 = data1.map(input_columns=['image'], operations=random_crop_and_resize_op)
    data2 = ds.TFRecordDataset(DATA_DIR, SCHEMA_DIR, columns_list=['image'], shuffle=False)
    data2 = data2.map(input_columns=['image'], operations=decode_op)
    num_iter = 0
    crop_and_resize_images = []
    original_images = []
    for item1, item2 in zip(data1.create_dict_iterator(num_epochs=1), data2.create_dict_iterator(num_epochs=1)):
        crop_and_resize = item1['image']
        original = item2['image']
        original = cv2.resize(original, (512, 256))
        mse = diff_mse(crop_and_resize, original)
        assert mse == 0
        logger.info('random_crop_and_resize_op_{}, mse: {}'.format(num_iter + 1, mse))
        num_iter += 1
        crop_and_resize_images.append(crop_and_resize)
        original_images.append(original)
    if plot:
        visualize_list(original_images, crop_and_resize_images)