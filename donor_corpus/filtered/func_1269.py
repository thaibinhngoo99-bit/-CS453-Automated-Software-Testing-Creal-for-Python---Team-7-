def get_more_images(imgs):
    more_images = []
    vert_flip_imgs = []
    hori_flip_imgs = []
    for i in range(0, imgs.shape[0]):
        a = imgs[i, :, :, 0]
        b = imgs[i, :, :, 1]
        av = cv2.flip(a, 1)
        ah = cv2.flip(a, 0)
        bv = cv2.flip(b, 1)
        bh = cv2.flip(b, 0)
        vert_flip_imgs.append(np.dstack((av, bv)))
        hori_flip_imgs.append(np.dstack((ah, bh)))
    v = np.array(vert_flip_imgs)
    h = np.array(hori_flip_imgs)
    more_images = np.concatenate((imgs, v, h))
    return more_images