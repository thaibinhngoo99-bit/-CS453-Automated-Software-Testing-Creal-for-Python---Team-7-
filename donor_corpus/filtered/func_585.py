def uiNewCombobox():
    """
    Creates a new combobox.

    :return: uiCombobox
    """
    clibui.uiNewCombobox.restype = ctypes.POINTER(uiCombobox)
    return clibui.uiNewCombobox()