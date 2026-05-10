def do_all(nb_epoch=30, batch_size=256):
    clf = CNNClassifier()
    x, y = clf.get_list()
    clf.train(x, y, nb_epoch=nb_epoch, batch_size=batch_size)
    clf.save()