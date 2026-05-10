def make_data_loader(phase, is_minknet, config):
    assert phase in ['train', 'val', 'test']
    is_train = phase == 'train'
    dataset = ModelNet40H5(phase=phase, transform=CoordinateTransformation(trans=config.translation) if is_train else CoordinateTranslation(config.test_translation), data_root='modelnet40_ply_hdf5_2048')
    return DataLoader(dataset, num_workers=config.num_workers, shuffle=is_train, collate_fn=minkowski_collate_fn if is_minknet else stack_collate_fn, batch_size=config.batch_size)