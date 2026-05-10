def _unzip_file_entry(zip_ref, file_entry, target_dir):
    """
    Extracts a Zipfile entry and preserves permissions
    """
    zip_ref.extract(file_entry.filename, path=target_dir)
    out_path = os.path.join(target_dir, file_entry.filename)
    perm = file_entry.external_attr >> 16
    os.chmod(out_path, perm or 511)