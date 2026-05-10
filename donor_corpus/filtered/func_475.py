def test_dice_overlap():
    radius_0 = 10.0
    radius_1 = 7.0
    centre_1 = 5.0
    sphere_0 = vtk.vtkSphereSource()
    sphere_0.SetRadius(radius_0)
    sphere_0.SetPhiResolution(60)
    sphere_0.SetThetaResolution(60)
    sphere_0.SetCenter(0.0, 0.0, 0.0)
    sphere_0.Update()
    vtk_model_0 = sphere_0.GetOutput()
    sphere_1 = vtk.vtkSphereSource()
    sphere_1.SetRadius(radius_1)
    sphere_1.SetPhiResolution(60)
    sphere_1.SetThetaResolution(60)
    sphere_1.SetCenter(centre_1, 0.0, 0.0)
    sphere_1.Update()
    vtk_model_1 = sphere_1.GetOutput()
    dice, volume_0, volume_1, volume_01 = pdu.two_polydata_dice(vtk_model_0, vtk_model_1)
    np.testing.assert_approx_equal(volume_0, 4.0 * np.pi * radius_0 ** 3.0 / 3.0, significant=2)
    np.testing.assert_approx_equal(volume_1, 4.0 * np.pi * radius_1 ** 3.0 / 3.0, significant=2)
    cap_height_0 = (radius_1 - radius_0 + centre_1) * (radius_1 + radius_0 - centre_1) / (2 * centre_1)
    cap_height_1 = (radius_0 - radius_1 + centre_1) * (radius_0 + radius_1 - centre_1) / (2 * centre_1)
    cap_vol_0 = np.pi * cap_height_0 ** 2 * (3 * radius_0 - cap_height_0) / 3
    cap_vol_1 = np.pi * cap_height_1 ** 2 * (3 * radius_1 - cap_height_1) / 3
    analytic = cap_vol_0 + cap_vol_1
    np.testing.assert_approx_equal(volume_01, analytic, significant=2)
    np.testing.assert_approx_equal(dice, 2 * volume_01 / (volume_0 + volume_1), significant=10)