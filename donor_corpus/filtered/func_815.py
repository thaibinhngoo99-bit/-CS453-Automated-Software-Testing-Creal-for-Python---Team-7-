def init_PySide2_QtDataVisualization():
    from PySide2.QtDataVisualization import QtDataVisualization
    QtDataVisualization.QBarDataRow = typing.List[QtDataVisualization.QBarDataItem]
    QtDataVisualization.QBarDataArray = typing.List[QtDataVisualization.QBarDataRow]
    QtDataVisualization.QSurfaceDataRow = typing.List[QtDataVisualization.QSurfaceDataItem]
    QtDataVisualization.QSurfaceDataArray = typing.List[QtDataVisualization.QSurfaceDataRow]
    type_map.update({'100.0f': 100.0, 'QtDataVisualization.QBarDataArray': QtDataVisualization.QBarDataArray, 'QtDataVisualization.QBarDataArray*': QtDataVisualization.QBarDataArray, 'QtDataVisualization.QSurfaceDataArray': QtDataVisualization.QSurfaceDataArray, 'QtDataVisualization.QSurfaceDataArray*': QtDataVisualization.QSurfaceDataArray})
    return locals()