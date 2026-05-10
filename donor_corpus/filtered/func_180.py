def set_shading_mode(mode='SOLID', screens=[]):
    """
    Performs an action analogous to clicking on the display/shade button of
    the 3D view. Mode is one of "RENDERED", "MATERIAL", "SOLID", "WIREFRAME".
    The change is applied to the given collection of bpy.data.screens.
    If none is given, the function is applied to bpy.context.screen (the
    active screen) only. E.g. set all screens to rendered mode:
      set_shading_mode("RENDERED", bpy.data.screens)
    """
    screens = screens if screens else [bpy.context.screen]
    for s in screens:
        for spc in s.areas:
            if spc.type == 'VIEW_3D':
                spc.spaces[0].shading.type = mode
                break