def resize(img):
    """
    Resize an image
        img: (ndarray) RGB color image
    """
    width = np.shape(img)[1]
    height = np.shape(img)[0]
    if width > RESIZE:
        scale = RESIZE / width
        resized_img = cv2.resize(img, (RESIZE, math.floor(height / scale)), cv2.INTER_AREA)
        return resized_img
    return img