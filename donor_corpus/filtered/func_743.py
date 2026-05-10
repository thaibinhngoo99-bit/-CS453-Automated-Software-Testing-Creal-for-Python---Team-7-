def create_mindrecord(dataset='coco', prefix='ssd.mindrecord', is_training=True):
    print('Start create dataset!')
    mindrecord_dir = config.mindrecord_dir
    mindrecord_file = os.path.join(mindrecord_dir, prefix + '0')
    if not os.path.exists(mindrecord_file):
        if not os.path.isdir(mindrecord_dir):
            os.makedirs(mindrecord_dir)
        if dataset == 'coco':
            if os.path.isdir(config.coco_root):
                print('Create Mindrecord.')
                data_to_mindrecord_byte_image('coco', is_training, prefix)
                print('Create Mindrecord Done, at {}'.format(mindrecord_dir))
            else:
                print('coco_root not exits.')
        elif dataset == 'voc':
            if os.path.isdir(config.voc_root):
                print('Create Mindrecord.')
                voc_data_to_mindrecord(mindrecord_dir, is_training, prefix)
                print('Create Mindrecord Done, at {}'.format(mindrecord_dir))
            else:
                print('voc_root not exits.')
        elif os.path.isdir(config.image_dir) and os.path.exists(config.anno_path):
            print('Create Mindrecord.')
            data_to_mindrecord_byte_image('other', is_training, prefix)
            print('Create Mindrecord Done, at {}'.format(mindrecord_dir))
        else:
            print('image_dir or anno_path not exits.')
    return mindrecord_file