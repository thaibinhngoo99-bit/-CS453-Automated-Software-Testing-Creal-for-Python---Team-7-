def verify_mapillary_tag(filepath):
    filepath_keep_original = processing.processed_images_rootpath(filepath)
    if os.path.isfile(filepath_keep_original):
        filepath = filepath_keep_original
    '\n    Check that image file has the required Mapillary tag\n    '
    return exif_read.ExifRead(filepath).mapillary_tag_exists()