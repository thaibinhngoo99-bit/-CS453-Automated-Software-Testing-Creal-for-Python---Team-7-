def calc_hash(img):
    """
    Calculate the wavelet hash of the image
        img: (ndarray) image file
    """
    img = resize(img)
    return imagehash.whash(Image.fromarray(img))