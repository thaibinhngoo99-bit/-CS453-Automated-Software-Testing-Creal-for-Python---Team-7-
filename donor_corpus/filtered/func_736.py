def create_voc_label(is_training):
    """Get image path and annotation from VOC."""
    voc_root = config.voc_root
    cls_map = {name: i for i, name in enumerate(config.classes)}
    sub_dir = 'train' if is_training else 'eval'
    voc_dir = os.path.join(voc_root, sub_dir)
    if not os.path.isdir(voc_dir):
        raise ValueError(f'Cannot find {sub_dir} dataset path.')
    image_dir = anno_dir = voc_dir
    if os.path.isdir(os.path.join(voc_dir, 'Images')):
        image_dir = os.path.join(voc_dir, 'Images')
    if os.path.isdir(os.path.join(voc_dir, 'Annotations')):
        anno_dir = os.path.join(voc_dir, 'Annotations')
    if not is_training:
        json_file = os.path.join(config.voc_root, config.voc_json)
        file_dir = os.path.split(json_file)[0]
        if not os.path.isdir(file_dir):
            os.makedirs(file_dir)
        json_dict = {'images': [], 'type': 'instances', 'annotations': [], 'categories': []}
        bnd_id = 1
    image_files_dict = {}
    image_anno_dict = {}
    images = []
    id_iter = 0
    for anno_file in os.listdir(anno_dir):
        print(anno_file)
        if not anno_file.endswith('xml'):
            continue
        tree = et.parse(os.path.join(anno_dir, anno_file))
        root_node = tree.getroot()
        file_name = root_node.find('filename').text
        img_id = get_imageId_from_fileName(file_name, id_iter)
        id_iter += 1
        image_path = os.path.join(image_dir, file_name)
        print(image_path)
        if not os.path.isfile(image_path):
            print(f'Cannot find image {file_name} according to annotations.')
            continue
        labels = []
        for obj in root_node.iter('object'):
            cls_name = obj.find('name').text
            if cls_name not in cls_map:
                print(f'Label "{cls_name}" not in "{config.classes}"')
                continue
            bnd_box = obj.find('bndbox')
            x_min = int(bnd_box.find('xmin').text) - 1
            y_min = int(bnd_box.find('ymin').text) - 1
            x_max = int(bnd_box.find('xmax').text) - 1
            y_max = int(bnd_box.find('ymax').text) - 1
            labels.append([y_min, x_min, y_max, x_max, cls_map[cls_name]])
            if not is_training:
                o_width = abs(x_max - x_min)
                o_height = abs(y_max - y_min)
                ann = {'area': o_width * o_height, 'iscrowd': 0, 'image_id': img_id, 'bbox': [x_min, y_min, o_width, o_height], 'category_id': cls_map[cls_name], 'id': bnd_id, 'ignore': 0, 'segmentation': []}
                json_dict['annotations'].append(ann)
                bnd_id = bnd_id + 1
        if labels:
            images.append(img_id)
            image_files_dict[img_id] = image_path
            image_anno_dict[img_id] = np.array(labels)
        if not is_training:
            size = root_node.find('size')
            width = int(size.find('width').text)
            height = int(size.find('height').text)
            image = {'file_name': file_name, 'height': height, 'width': width, 'id': img_id}
            json_dict['images'].append(image)
    if not is_training:
        for cls_name, cid in cls_map.items():
            cat = {'supercategory': 'none', 'id': cid, 'name': cls_name}
            json_dict['categories'].append(cat)
        json_fp = open(json_file, 'w')
        json_str = json.dumps(json_dict)
        json_fp.write(json_str)
        json_fp.close()
    return (images, image_files_dict, image_anno_dict)