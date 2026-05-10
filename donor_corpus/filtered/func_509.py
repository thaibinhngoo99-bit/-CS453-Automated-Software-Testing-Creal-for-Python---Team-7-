def test_random_crop_and_resize_op_py(plot=False):
    """
    Test RandomCropAndResize op in py transforms
    """
    logger.info('test_random_crop_and_resize_op_py')
    data1 = ds.TFRecordDataset(DATA_DIR, SCHEMA_DIR, columns_list=['image'], shuffle=False)
    transforms1 = [py_vision.Decode(), py_vision.RandomResizedCrop((256, 512), (2, 2), (1, 3)), py_vision.ToTensor()]
    transform1 = mindspore.dataset.transforms.py_transforms.Compose(transforms1)
    data1 = data1.map(input_columns=['image'], operations=transform1)
    data2 = ds.TFRecordDataset(DATA_DIR, SCHEMA_DIR, columns_list=['image'], shuffle=False)
    transforms2 = [py_vision.Decode(), py_vision.ToTensor()]
    transform2 = mindspore.dataset.transforms.py_transforms.Compose(transforms2)
    data2 = data2.map(input_columns=['image'], operations=transform2)
    num_iter = 0
    crop_and_resize_images = []
    original_images = []
    for item1, item2 in zip(data1.create_dict_iterator(num_epochs=1), data2.create_dict_iterator(num_epochs=1)):
        crop_and_resize = (item1['image'].transpose(1, 2, 0) * 255).astype(np.uint8)
        original = (item2['image'].transpose(1, 2, 0) * 255).astype(np.uint8)
        original = cv2.resize(original, (512, 256))
        mse = diff_mse(crop_and_resize, original)
        assert mse <= 0.05
        logger.info('random_crop_and_resize_op_{}, mse: {}'.format(num_iter + 1, mse))
        num_iter += 1
        crop_and_resize_images.append(crop_and_resize)
        original_images.append(original)
    if plot:
        visualize_list(original_images, crop_and_resize_images)