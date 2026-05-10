def hamming(y_true, y_pred, axis=(1, 2, 3)):
    y_pred = tf.convert_to_tensor(y_pred)
    y_true = tf.cast(y_true, y_pred.dtype)
    return tf.reduce_mean(tf.not_equal(y_pred, y_true), axis=axis)