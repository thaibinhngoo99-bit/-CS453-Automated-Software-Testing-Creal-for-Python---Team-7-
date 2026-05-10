def init_PySide2_QtCore():
    from PySide2.QtCore import Qt, QUrl, QDir
    from PySide2.QtCore import QRect, QSize, QPoint, QLocale, QByteArray
    from PySide2.QtCore import QMarginsF
    try:
        from PySide2.QtCore import Connection
    except ImportError:
        pass
    type_map.update({"' '": ' ', "'%'": '%', "'g'": 'g', '4294967295UL': 4294967295, 'CheckIndexOption.NoOption': Instance('PySide2.QtCore.QAbstractItemModel.CheckIndexOptions.NoOption'), 'DescriptorType(-1)': int, 'false': False, 'list of QAbstractAnimation': typing.List[PySide2.QtCore.QAbstractAnimation], 'list of QAbstractState': typing.List[PySide2.QtCore.QAbstractState], 'long long': int, 'NULL': None, 'nullptr': None, 'PyByteArray': bytearray, 'PyBytes': bytes, 'QDeadlineTimer(QDeadlineTimer.Forever)': Instance('PySide2.QtCore.QDeadlineTimer'), 'PySide2.QtCore.QUrl.ComponentFormattingOptions': PySide2.QtCore.QUrl.ComponentFormattingOption, 'PyUnicode': typing.Text, 'Q_NULLPTR': None, 'QDir.Filters(AllEntries | NoDotAndDotDot)': Instance('QDir.Filters(QDir.AllEntries | QDir.NoDotAndDotDot)'), 'QDir.SortFlags(Name | IgnoreCase)': Instance('QDir.SortFlags(QDir.Name | QDir.IgnoreCase)'), 'QGenericArgument((0))': ellipsis, 'QGenericArgument()': ellipsis, 'QGenericArgument(0)': ellipsis, 'QGenericArgument(NULL)': ellipsis, 'QGenericArgument(nullptr)': ellipsis, 'QGenericArgument(Q_NULLPTR)': ellipsis, 'QJsonObject': typing.Dict[str, PySide2.QtCore.QJsonValue], 'QModelIndex()': Invalid('PySide2.QtCore.QModelIndex'), 'QModelIndexList': ModelIndexList, 'QModelIndexList': ModelIndexList, 'QString()': '', 'QStringList()': [], 'QStringRef': str, 'QStringRef': str, 'Qt.HANDLE': int, 'QUrl.FormattingOptions(PrettyDecoded)': Instance('QUrl.FormattingOptions(QUrl.PrettyDecoded)'), 'QVariant()': Invalid(Variant), 'QVariant.Type': type, 'QVariantMap': typing.Dict[str, Variant], 'QVariantMap': typing.Dict[str, Variant]})
    try:
        type_map.update({'PySide2.QtCore.QMetaObject.Connection': PySide2.QtCore.Connection})
    except AttributeError:
        pass
    return locals()