def _get_device_args(options):
    flash_runner = _get_flash_runner()
    if flash_runner == 'nrfjprog':
        return _get_nrf_device_args(options)
    if flash_runner == 'openocd':
        return _get_openocd_device_args(options)
    raise BoardError(f"Don't know how to find serial terminal for board {CMAKE_CACHE['BOARD']} with flash runner {flash_runner}")