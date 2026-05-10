def get_repo_tag_meta(meta_conf):
    repotag = meta_conf.get('repotag')
    if repotag:
        return repotag
    if 'go' in meta_conf['autorest_options']:
        return 'azure-sdk-for-go'
    if 'ruby' in meta_conf['autorest_options']:
        return 'azure-sdk-for-ruby'
    if 'java' in meta_conf['autorest_options']:
        return 'azure-sdk-for-java'
    if 'nodejs' in meta_conf['autorest_options']:
        return 'azure-sdk-for-node'
    if 'typescript' in meta_conf['autorest_options']:
        return 'azure-sdk-for-js'
    raise ValueError('No repotag found or infered')