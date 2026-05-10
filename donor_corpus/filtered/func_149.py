def tversky(y_true, y_pred, axis=(1, 2, 3), alpha=0.3, beta=0.7):
    y_pred = tf.convert_to_tensor(y_pred)
    y_true = tf.cast(y_true, y_pred.dtype)
    if y_true.get_shape().ndims < 2 or y_pred.get_shape().ndims < 2:
        raise ValueError('y_true and y_pred must be at least rank 2.')
    eps = tf.keras.backend.epsilon()
    num = tf.reduce_sum(y_pred * y_true, axis=axis)
    den = num + alpha * tf.reduce_sum(y_pred * (1 - y_true), axis=axis) + beta * tf.reduce_sum((1 - y_pred) * y_true, axis=axis)
    return tf.reduce_sum((num + eps) / (den + eps), axis=-1)