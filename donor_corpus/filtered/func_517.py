def test_random_crop_and_resize_comp(plot=False):
    """
    Test RandomCropAndResize and compare between python and c image augmentation
    """
    logger.info('test_random_crop_and_resize_comp')
    data1 = ds.TFRecordDataset(DATA_DIR, SCHEMA_DIR, columns_list=['image'], shuffle=False)
    decode_op = c_vision.Decode()
    random_crop_and_resize_op = c_vision.RandomResizedCrop(512, (1, 1), (0.5, 0.5))
    data1 = data1.map(input_columns=['image'], operations=decode_op)
    data1 = data1.map(input_columns=['image'], operations=random_crop_and_resize_op)
    data2 = ds.TFRecordDataset(DATA_DIR, SCHEMA_DIR, columns_list=['image'], shuffle=False)
    transforms = [py_vision.Decode(), py_vision.RandomResizedCrop(512, (1, 1), (0.5, 0.5)), py_vision.ToTensor()]
    transform = mindspore.dataset.transforms.py_transforms.Compose(transforms)
    data2 = data2.map(input_columns=['image'], operations=transform)
    image_c_cropped = []
    image_py_cropped = []
    for item1, item2 in zip(data1.create_dict_iterator(num_epochs=1), data2.create_dict_iterator(num_epochs=1)):
        c_image = item1['image']
        py_image = (item2['image'].transpose(1, 2, 0) * 255).astype(np.uint8)
        image_c_cropped.append(c_image)
        image_py_cropped.append(py_image)
        mse = diff_mse(c_image, py_image)
        assert mse < 0.02
    if plot:
        visualize_list(image_c_cropped, image_py_cropped, visualize_mode=2)