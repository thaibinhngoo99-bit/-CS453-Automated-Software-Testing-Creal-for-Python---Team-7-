def generalized_dice(y_true, y_pred, axis=(1, 2, 3)):
    """Calculate Generalized Dice similarity. This is useful for multi-class
    predictions.

    If we assume the inputs are rank 5 [`(batch, x, y, z, classes)`], then an
    axis parameter of `(1, 2, 3)` should be used. This will result in a tensor
    of shape `(batch,)`, where every value is the Generalized Dice similarity
    for that prediction, across all classes.

    Returns
    -------
    Tensor of Generalized Dice similarities.
    """
    y_pred = tf.convert_to_tensor(y_pred)
    y_true = tf.cast(y_true, y_pred.dtype)
    if y_true.get_shape().ndims < 2 or y_pred.get_shape().ndims < 2:
        raise ValueError('y_true and y_pred must be at least rank 2.')
    epsilon = tf.keras.backend.epsilon()
    w = tf.math.reciprocal(tf.square(tf.reduce_sum(y_true, axis=axis)))
    w = tf.where(tf.math.is_finite(w), w, epsilon)
    num = 2 * tf.reduce_sum(w * tf.reduce_sum(y_true * y_pred, axis=axis), axis=-1)
    den = tf.reduce_sum(w * tf.reduce_sum(y_true + y_pred, axis=axis), axis=-1)
    gdice = num / den
    gdice = tf.where(tf.math.is_finite(gdice), gdice, tf.zeros_like(gdice))
    return gdice