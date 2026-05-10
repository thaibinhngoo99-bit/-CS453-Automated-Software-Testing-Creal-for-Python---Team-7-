def init_PySide2_QtXmlPatterns():
    from PySide2.QtXmlPatterns import QXmlName
    type_map.update({'QXmlName.NamespaceCode': Missing('PySide2.QtXmlPatterns.QXmlName.NamespaceCode'), 'QXmlName.PrefixCode': Missing('PySide2.QtXmlPatterns.QXmlName.PrefixCode')})
    return locals()