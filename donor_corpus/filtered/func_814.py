def init_PySide2_QtMultimedia():
    import PySide2.QtMultimediaWidgets
    check_module(PySide2.QtMultimediaWidgets)
    type_map.update({'QGraphicsVideoItem': PySide2.QtMultimediaWidgets.QGraphicsVideoItem, 'qint64': int, 'QVideoWidget': PySide2.QtMultimediaWidgets.QVideoWidget})
    return locals()