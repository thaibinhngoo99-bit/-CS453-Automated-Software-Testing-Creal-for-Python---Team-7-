def init_PySide2_QtNetwork():
    from PySide2.QtNetwork import QNetworkRequest
    best_structure = typing.OrderedDict if getattr(typing, 'OrderedDict', None) else typing.Dict
    type_map.update({'QMultiMap[PySide2.QtNetwork.QSsl.AlternativeNameEntryType, QString]': best_structure[PySide2.QtNetwork.QSsl.AlternativeNameEntryType, typing.List[str]], 'DefaultTransferTimeoutConstant': QNetworkRequest.TransferTimeoutConstant, 'QNetworkRequest.DefaultTransferTimeoutConstant': QNetworkRequest.TransferTimeoutConstant})
    del best_structure
    return locals()