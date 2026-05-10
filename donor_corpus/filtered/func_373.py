def result(img):
    img = img.reshape(1, 784)
    img = img.astype(np.float32)
    img = np.multiply(img, 1.0 / 255.0)
    pred = remote.execute('http://localhost:9001', img)
    r = np.argmax(pred, axis=1)
    pp = pred * 100
    top1 = str(np.argsort(-pp)[0][0]) + ' (' + str(int(np.sort(-pp)[0][0] * -1)) + '%)'
    top2 = str(np.argsort(-pp)[0][1]) + ' (' + str(int(np.sort(-pp)[0][1] * -1)) + '%)'
    top3 = str(np.argsort(-pp)[0][2]) + ' (' + str(int(np.sort(-pp)[0][2] * -1)) + '%)'
    return (r, top1, top2, top3)