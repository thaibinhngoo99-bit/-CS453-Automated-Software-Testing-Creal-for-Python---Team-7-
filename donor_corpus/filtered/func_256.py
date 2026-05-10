def load_images(dirname):
    images = []
    for image_name in os.listdir(dirname):
        if image_name.startswith('.'):
            continue
        image = Image.open(dirname + '/' + image_name).convert('1')
        x, y = image.size
        image = image.resize((x, 280), Image.ANTIALIAS)
        data = [0 if pixel == 0 else 1 for pixel in image.getdata()]
        images.append(data)
    return images