def random_sample_crop(image, boxes):
    """Random Crop the image and boxes"""
    height, width, _ = image.shape
    min_iou = np.random.choice([None, 0.1, 0.3, 0.5, 0.7, 0.9])
    if min_iou is None:
        return (image, boxes)
    for _ in range(50):
        image_t = image
        w = _rand(0.3, 1.0) * width
        h = _rand(0.3, 1.0) * height
        if h / w < 0.5 or h / w > 2:
            continue
        left = _rand() * (width - w)
        top = _rand() * (height - h)
        rect = np.array([int(top), int(left), int(top + h), int(left + w)])
        overlap = jaccard_numpy(boxes, rect)
        drop_mask = overlap > 0
        if not drop_mask.any():
            continue
        if overlap[drop_mask].min() < min_iou and overlap[drop_mask].max() > min_iou + 0.2:
            continue
        image_t = image_t[rect[0]:rect[2], rect[1]:rect[3], :]
        centers = (boxes[:, :2] + boxes[:, 2:4]) / 2.0
        m1 = (rect[0] < centers[:, 0]) * (rect[1] < centers[:, 1])
        m2 = (rect[2] > centers[:, 0]) * (rect[3] > centers[:, 1])
        mask = m1 * m2 * drop_mask
        if not mask.any():
            continue
        boxes_t = boxes[mask, :].copy()
        boxes_t[:, :2] = np.maximum(boxes_t[:, :2], rect[:2])
        boxes_t[:, :2] -= rect[:2]
        boxes_t[:, 2:4] = np.minimum(boxes_t[:, 2:4], rect[2:4])
        boxes_t[:, 2:4] -= rect[:2]
        return (image_t, boxes_t)
    return (image, boxes)