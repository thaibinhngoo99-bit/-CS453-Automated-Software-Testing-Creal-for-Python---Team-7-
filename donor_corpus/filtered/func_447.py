def classifier(base_layers, input_rois, num_rois, nb_classes=21, trainable=False):
    if K.backend() == 'tensorflow':
        pooling_regions = 14
        input_shape = (num_rois, 14, 14, 1024)
    elif K.backend() == 'theano':
        pooling_regions = 7
        input_shape = (num_rois, 4096, 7, 7)
    out_roi_pool = RoiPoolingConv(pooling_regions, num_rois)([base_layers, input_rois])
    out_roi_pool = TimeDistributed(AveragePooling2D((7, 7)), name='avg_pool')(out_roi_pool)
    out = TimeDistributed(Flatten(name='flatten'))(out_roi_pool)
    out = TimeDistributed(Dense(4096, activation='relu', name='fc1'))(out)
    out = TimeDistributed(Dropout(0.5))(out)
    out = TimeDistributed(Dense(4096, activation='relu', name='fc2'))(out)
    out = TimeDistributed(Dropout(0.5))(out)
    out_class = TimeDistributed(Dense(nb_classes, activation='softmax', kernel_initializer='zero'), name='dense_class_{}'.format(nb_classes))(out)
    out_regr = TimeDistributed(Dense(4 * (nb_classes - 1), activation='linear', kernel_initializer='zero'), name='dense_regress_{}'.format(nb_classes))(out)
    return [out_class, out_regr]