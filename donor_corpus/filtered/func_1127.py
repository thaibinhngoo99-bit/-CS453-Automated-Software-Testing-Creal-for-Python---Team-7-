def is_jar_archive(content):
    """ Determine whether `content` contains valid zip bytes representing a JAR archive
        that contains at least one *.class file and a META-INF/MANIFEST.MF file. """
    try:
        with tempfile.NamedTemporaryFile() as tf:
            tf.write(content)
            tf.flush()
            with zipfile.ZipFile(tf.name, 'r') as zf:
                class_files = [e for e in zf.infolist() if e.filename.endswith('.class')]
                manifest_file = [e for e in zf.infolist() if e.filename.upper() == 'META-INF/MANIFEST.MF']
                if not class_files or not manifest_file:
                    return False
    except Exception:
        return False
    return True