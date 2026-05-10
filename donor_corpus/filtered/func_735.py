def preprocess_fn(img_id, image, box, is_training):
    """Preprocess function for dataset."""
    cv2.setNumThreads(2)

    def _infer_data(image, input_shape):
        img_h, img_w, _ = image.shape
        input_h, input_w = input_shape
        image = cv2.resize(image, (input_w, input_h))
        if len(image.shape) == 2:
            image = np.expand_dims(image, axis=-1)
            image = np.concatenate([image, image, image], axis=-1)
        return (img_id, image, np.array((img_h, img_w), np.float32))

    def _data_aug(image, box, is_training, image_size=(300, 300)):
        """Data augmentation function."""
        ih, iw, _ = image.shape
        w, h = image_size
        if not is_training:
            return _infer_data(image, image_size)
        box = box.astype(np.float32)
        image, box = random_sample_crop(image, box)
        ih, iw, _ = image.shape
        image = cv2.resize(image, (w, h))
        flip = _rand() < 0.5
        if flip:
            image = cv2.flip(image, 1, dst=None)
        if len(image.shape) == 2:
            image = np.expand_dims(image, axis=-1)
            image = np.concatenate([image, image, image], axis=-1)
        box[:, [0, 2]] = box[:, [0, 2]] / ih
        box[:, [1, 3]] = box[:, [1, 3]] / iw
        if flip:
            box[:, [1, 3]] = 1 - box[:, [3, 1]]
        box, label, num_match = ssd_bboxes_encode(box)
        return (image, box, label, num_match)
    return _data_aug(image, box, is_training, image_size=config.img_shape)