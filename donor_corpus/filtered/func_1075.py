def get_exec_version(path):
    ver_cmd = [path, '--version']
    try:
        version = subprocess.check_output(ver_cmd).decode('utf-8')
        version = version.lower().split('version')[-1].strip()
    except:
        version = '0.0.1'
    return version