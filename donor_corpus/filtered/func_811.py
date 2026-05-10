def init_PySide2_QtSql():
    from PySide2.QtSql import QSqlDatabase
    type_map.update({'QLatin1String(defaultConnection)': QSqlDatabase.defaultConnection, 'QVariant.Invalid': Invalid('Variant')})
    return locals()