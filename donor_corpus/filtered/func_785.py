def build_images(x):
    images = np.zeros((len(x), 64, 64, 3))
    for idx, img_fname in enumerate(x):
        im = cv2.imread(img_fname)
        im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        im = cv2.resize(im, (64, 64), interpolation=cv2.INTER_AREA)
        images[idx] = im
    return images