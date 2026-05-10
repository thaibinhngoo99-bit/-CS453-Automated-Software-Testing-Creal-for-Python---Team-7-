def build_file_content():
    autorest_version = autorest_latest_version_finder()
    autorest_bootstrap_version = autorest_bootstrap_version_finder()
    return {'autorest': autorest_version, 'autorest_bootstrap': autorest_bootstrap_version}