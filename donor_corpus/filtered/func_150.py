def dice_coef_multilabel(y_true, y_pred):
    n_classes = tf.shape(y_pred)[-1]
    dice_coeff = 0
    for index in range(n_classes):
        dice_coeff -= dice(y_true[:, :, :, :, index], y_pred[:, :, :, :, index])
    return dice_coeff