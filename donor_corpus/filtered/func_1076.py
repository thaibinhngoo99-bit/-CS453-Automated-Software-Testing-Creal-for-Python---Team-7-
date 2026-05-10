def last_julia_version(version=None):

    def sort_key(ver):
        return float(ver.lstrip('v'))
    version = float(f_minor_version(version)) if version else 999.999
    proj_versions = os.listdir(os.path.join(default_depot_path(), 'environments'))
    proj_versions = [x for x in proj_versions if re.fullmatch('v\\d+\\.\\d+', x)]
    proj_versions = sorted(filter(lambda ver: sort_key(ver) < version, proj_versions), key=sort_key)
    if proj_versions:
        return proj_versions[-1]
    else:
        return None