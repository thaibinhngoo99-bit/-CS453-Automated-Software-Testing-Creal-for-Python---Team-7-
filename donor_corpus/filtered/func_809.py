def init_PySide2_QtGui():
    from PySide2.QtGui import QPageLayout, QPageSize
    type_map.update({'0.0f': 0.0, '1.0f': 1.0, 'GL_COLOR_BUFFER_BIT': GL_COLOR_BUFFER_BIT, 'GL_NEAREST': GL_NEAREST, 'int32_t': int, 'QPixmap()': Default('PySide2.QtGui.QPixmap'), 'QPlatformSurface*': int, 'QVector< QTextLayout.FormatRange >()': [], 'uint32_t': int, 'uint8_t': int, 'USHRT_MAX': ushort_max})
    return locals()