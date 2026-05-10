def filter_valid_data(image_dir, anno_path):
    """Filter valid image file, which both in image_dir and anno_path."""
    images = []
    image_path_dict = {}
    image_anno_dict = {}
    if not os.path.isdir(image_dir):
        raise RuntimeError('Path given is not valid.')
    if not os.path.isfile(anno_path):
        raise RuntimeError('Annotation file is not valid.')
    with open(anno_path, 'rb') as f:
        lines = f.readlines()
    for img_id, line in enumerate(lines):
        line_str = line.decode('utf-8').strip()
        line_split = str(line_str).split(' ')
        file_name = line_split[0]
        image_path = os.path.join(image_dir, file_name)
        if os.path.isfile(image_path):
            images.append(img_id)
            image_path_dict[img_id] = image_path
            image_anno_dict[img_id] = anno_parser(line_split[1:])
    return (images, image_path_dict, image_anno_dict)