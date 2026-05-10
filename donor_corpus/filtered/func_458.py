def _get_flash_runner():
    flash_runner = CMAKE_CACHE.get('ZEPHYR_BOARD_FLASH_RUNNER')
    if flash_runner is not None:
        return flash_runner
    with open(CMAKE_CACHE['ZEPHYR_RUNNERS_YAML']) as f:
        doc = yaml.load(f, Loader=yaml.FullLoader)
    return doc['flash-runner']