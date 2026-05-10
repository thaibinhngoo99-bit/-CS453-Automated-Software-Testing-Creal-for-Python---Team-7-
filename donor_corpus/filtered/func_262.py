def main(edge_dir, non_edge_dir):
    edges = load_images(edge_dir)
    nonedges = load_images(non_edge_dir)
    crossvalidate(edges, nonedges)
    clf = train(edges, nonedges)
    for comic in os.listdir('test'):
        print(comic)
        panels, matches = search_picture(clf, 'test/' + comic)
        print('\tpanels: {}'.format(panels))
        image = Image.open('test/' + comic).convert('RGBA')
        draw = ImageDraw.Draw(image)
        w, h = image.size
        for match in matches:
            match = match[0]
            draw.line((match, 0) + (match, h), fill=(0, 0, 255, 0))
        for sep in panels:
            draw.line((sep, 0) + (sep, h), fill=(255, 0, 0), width=3)
        image.show()
    return clf