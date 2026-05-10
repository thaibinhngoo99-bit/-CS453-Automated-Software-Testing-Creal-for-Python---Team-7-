def set_cam_intrinsic(cam, intrinsic_K, hw=None):
    """
    K = [[f_x, 0, c_x],
     [0, f_y, c_y],
     [0,   0,   1]]

    Refrence: https://www.rojtberg.net/1601/from-blender-to-opencv-camera-and-back/
    """
    if hw is None:
        scene = bpy.context.scene
        hw = (scene.render.resolution_y, scene.render.resolution_x)
    near = lambda x, y=0, eps=1e-05: abs(x - y) < eps
    assert near(intrinsic_K[0][1], 0)
    assert near(intrinsic_K[1][0], 0)
    h, w = hw
    f_x = intrinsic_K[0][0]
    f_y = intrinsic_K[1][1]
    c_x = intrinsic_K[0][2]
    c_y = intrinsic_K[1][2]
    cam = cam.data
    cam.shift_x = -(c_x / w - 0.5)
    cam.shift_y = (c_y - 0.5 * h) / w
    cam.lens = f_x / w * cam.sensor_width
    pixel_aspect = f_y / f_x
    scene.render.pixel_aspect_x = 1.0
    scene.render.pixel_aspect_y = pixel_aspect