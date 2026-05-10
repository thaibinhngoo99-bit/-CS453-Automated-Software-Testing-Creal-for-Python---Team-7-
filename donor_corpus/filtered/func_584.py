def uiComboboxOnSelected(combobox, callback, data):
    """
    Executes a callback function when an item selected.

    :param combobox: uiCombobox
    :param callback: function
    :param data: data
    :return: reference to C callback function
    """
    c_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(uiCombobox), ctypes.c_void_p)
    c_callback = c_type(callback)
    clibui.uiComboboxOnSelected(combobox, c_callback, data)
    return c_callback