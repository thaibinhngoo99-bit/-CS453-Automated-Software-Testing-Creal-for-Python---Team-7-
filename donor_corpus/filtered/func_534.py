def classFactory(iface):
    """Load SimplePhotogrammetryRoutePlanner class from file SimplePhotogrammetryRoutePlanner.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    from .SimplePhotogrammetryRoutePlanner import SimplePhotogrammetryRoutePlanner
    return SimplePhotogrammetryRoutePlanner(iface)