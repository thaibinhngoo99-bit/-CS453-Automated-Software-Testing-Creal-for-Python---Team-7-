def get_answer(req):
    img_str = re.search('base64,(.*)', req.form['img']).group(1)
    nparr = np.fromstring(base64.b64decode(img_str), np.uint8)
    img_src = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img_negaposi = 255 - img_src
    img_gray = cv2.cvtColor(img_negaposi, cv2.COLOR_BGR2GRAY)
    img_resize = cv2.resize(img_gray, (28, 28))
    cv2.imwrite(f'images/{datetime.now().strftime('%s')}.jpg', img_resize)
    ans, t1, t2, t3 = result(img_resize)
    return (int(ans), t1, t2, t3)