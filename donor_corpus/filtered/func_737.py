def create_coco_label(is_training):
    """Get image path and annotation from COCO."""
    from pycocotools.coco import COCO
    coco_root = config.coco_root
    data_type = config.val_data_type
    if is_training:
        data_type = config.train_data_type
    train_cls = config.classes
    train_cls_dict = {}
    for i, cls in enumerate(train_cls):
        train_cls_dict[cls] = i
    anno_json = os.path.join(coco_root, config.instances_set.format(data_type))
    coco = COCO(anno_json)
    classs_dict = {}
    cat_ids = coco.loadCats(coco.getCatIds())
    for cat in cat_ids:
        classs_dict[cat['id']] = cat['name']
    image_ids = coco.getImgIds()
    images = []
    image_path_dict = {}
    image_anno_dict = {}
    for img_id in image_ids:
        image_info = coco.loadImgs(img_id)
        file_name = image_info[0]['file_name']
        anno_ids = coco.getAnnIds(imgIds=img_id, iscrowd=None)
        anno = coco.loadAnns(anno_ids)
        image_path = os.path.join(coco_root, data_type, file_name)
        annos = []
        iscrowd = False
        for label in anno:
            bbox = label['bbox']
            class_name = classs_dict[label['category_id']]
            iscrowd = iscrowd or label['iscrowd']
            if class_name in train_cls:
                x_min, x_max = (bbox[0], bbox[0] + bbox[2])
                y_min, y_max = (bbox[1], bbox[1] + bbox[3])
                annos.append(list(map(round, [y_min, x_min, y_max, x_max])) + [train_cls_dict[class_name]])
        if not is_training and iscrowd:
            continue
        if len(annos) >= 1:
            images.append(img_id)
            image_path_dict[img_id] = image_path
            image_anno_dict[img_id] = np.array(annos)
    return (images, image_path_dict, image_anno_dict)