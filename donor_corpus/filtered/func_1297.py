def merge_boxes(box1, box2):
    """Merges two boxes."""
    (x_min1, x_max1), (y_min1, y_max1), (z_min1, z_max1) = box1
    (x_min2, x_max2), (y_min2, y_max2), (z_min2, z_max2) = box2
    x_min = min(x_min1, x_min2)
    y_min = min(y_min1, y_min2)
    z_min = min(z_min1, z_min2)
    x_max = max(x_max1, x_max2)
    y_max = max(y_max1, y_max2)
    z_max = max(z_max1, z_max2)
    return ((x_min, x_max), (y_min, y_max), (z_min, z_max))