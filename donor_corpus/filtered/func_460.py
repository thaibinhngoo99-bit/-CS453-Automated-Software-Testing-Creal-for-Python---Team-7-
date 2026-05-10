def openocd_serial(options):
    """Find the serial port to use for a board with OpenOCD flash strategy."""
    if 'openocd_serial' in options:
        return options['openocd_serial']
    import usb
    find_kw = BOARD_USB_FIND_KW[CMAKE_CACHE['BOARD']]
    boards = usb.core.find(find_all=True, **find_kw)
    serials = []
    for b in boards:
        serials.append(b.serial_number)
    if len(serials) == 0:
        raise BoardAutodetectFailed(f'No attached USB devices matching: {find_kw!r}')
    serials.sort()
    autodetected_openocd_serial = serials[0]
    _LOG.debug('zephyr openocd driver: autodetected serial %s', serials[0])
    return autodetected_openocd_serial