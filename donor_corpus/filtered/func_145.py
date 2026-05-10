def dice(y_true, y_pred, axis=(1, 2, 3, 4)):
    """Calculate Dice similarity between labels and predictions.

    Dice similarity is in [0, 1], where 1 is perfect overlap and 0 is no
    overlap. If both labels and predictions are empty (e.g., all background),
    then Dice similarity is 1.

    If we assume the inputs are rank 5 [`(batch, x, y, z, classes)`], then an
    axis parameter of `(1, 2, 3)` will result in a tensor that contains a Dice
    score for every class in every item in the batch. The shape of this tensor
    will be `(batch, classes)`. If the inputs only have one class (e.g., binary
    segmentation), then an axis parameter of `(1, 2, 3, 4)` should be used.
    This will result in a tensor of shape `(batch,)`, where every value is the
    Dice similarity for that prediction.

    Implemented according to https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4533825/#Equ6

    Returns
    -------
    Tensor of Dice similarities.

    Citations
    ---------
    Taha AA, Hanbury A. Metrics for evaluating 3D medical image segmentation:
        analysis, selection, and tool. BMC Med Imaging. 2015;15:29. Published 2015
        Aug 12. doi:10.1186/s12880-015-0068-x
    """
    y_pred = tf.convert_to_tensor(y_pred)
    y_true = tf.cast(y_true, y_pred.dtype)
    eps = tf.keras.backend.epsilon()
    intersection = tf.reduce_sum(y_true * y_pred, axis=axis)
    summation = tf.reduce_sum(y_true, axis=axis) + tf.reduce_sum(y_pred, axis=axis)
    return (2 * intersection + eps) / (summation + eps)