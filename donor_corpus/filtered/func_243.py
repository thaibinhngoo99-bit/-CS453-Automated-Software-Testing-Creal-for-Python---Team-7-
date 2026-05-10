def hue_shift(image, value):
    im = image.convert('RGBA')
    arr = np.array(np.asarray(im).astype(float))
    r, g, b, a = np.rollaxis(arr, axis=-1)
    h, s, v = rgb_to_hsv(r, g, b)
    r, g, b = hsv_to_rgb((h + value / 360.0) % 1.0, s, v)
    arr = np.dstack((r, g, b, a))
    return Image.fromarray(arr.astype('uint8'), 'RGBA')