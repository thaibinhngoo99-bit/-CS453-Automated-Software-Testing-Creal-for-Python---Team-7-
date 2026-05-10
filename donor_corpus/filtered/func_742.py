def create_ssd_dataset(mindrecord_file, batch_size=32, repeat_num=10, device_num=1, rank=0, is_training=True, num_parallel_workers=4, use_multiprocessing=True):
    """Create SSD dataset with MindDataset."""
    ds = de.MindDataset(mindrecord_file, columns_list=['img_id', 'image', 'annotation'], num_shards=device_num, shard_id=rank, num_parallel_workers=num_parallel_workers, shuffle=is_training)
    decode = C.Decode()
    ds = ds.map(operations=decode, input_columns=['image'])
    change_swap_op = C.HWC2CHW()
    normalize_op = C.Normalize(mean=[0.485 * 255, 0.456 * 255, 0.406 * 255], std=[0.229 * 255, 0.224 * 255, 0.225 * 255])
    color_adjust_op = C.RandomColorAdjust(brightness=0.4, contrast=0.4, saturation=0.4)
    compose_map_func = lambda img_id, image, annotation: preprocess_fn(img_id, image, annotation, is_training)
    if is_training:
        output_columns = ['image', 'box', 'label', 'num_match']
        trans = [color_adjust_op, normalize_op, change_swap_op]
    else:
        output_columns = ['img_id', 'image', 'image_shape']
        trans = [normalize_op, change_swap_op]
    ds = ds.map(operations=compose_map_func, input_columns=['img_id', 'image', 'annotation'], output_columns=output_columns, column_order=output_columns, python_multiprocessing=use_multiprocessing, num_parallel_workers=num_parallel_workers)
    ds = ds.map(operations=trans, input_columns=['image'], python_multiprocessing=use_multiprocessing, num_parallel_workers=num_parallel_workers)
    ds = ds.batch(batch_size, drop_remainder=True)
    ds = ds.repeat(repeat_num)
    return ds