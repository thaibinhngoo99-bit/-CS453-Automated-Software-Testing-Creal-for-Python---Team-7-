def data_to_mindrecord_byte_image(dataset='coco', is_training=True, prefix='ssd.mindrecord', file_num=8):
    """Create MindRecord file."""
    mindrecord_dir = config.mindrecord_dir
    mindrecord_path = os.path.join(mindrecord_dir, prefix)
    writer = FileWriter(mindrecord_path, file_num)
    if dataset == 'coco':
        images, image_path_dict, image_anno_dict = create_coco_label(is_training)
    else:
        images, image_path_dict, image_anno_dict = filter_valid_data(config.image_dir, config.anno_path)
    ssd_json = {'img_id': {'type': 'int32', 'shape': [1]}, 'image': {'type': 'bytes'}, 'annotation': {'type': 'int32', 'shape': [-1, 5]}}
    writer.add_schema(ssd_json, 'ssd_json')
    for img_id in images:
        image_path = image_path_dict[img_id]
        with open(image_path, 'rb') as f:
            img = f.read()
        annos = np.array(image_anno_dict[img_id], dtype=np.int32)
        img_id = np.array([img_id], dtype=np.int32)
        row = {'img_id': img_id, 'image': img, 'annotation': annos}
        writer.write_raw_data([row])
    writer.commit()