def get_column(img, i):
    w, h = img.size
    column = []
    for j in range(h):
        column.append(0 if img.getpixel((i, j)) == 0 else 1)
    return column