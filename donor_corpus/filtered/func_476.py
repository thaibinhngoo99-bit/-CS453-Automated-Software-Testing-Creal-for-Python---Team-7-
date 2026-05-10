def test_dice_no_overlap():
    radius_0 = 5.5
    radius_1 = 4.3
    centre_1 = 12.0
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
    analytic = 0.0
    np.testing.assert_approx_equal(volume_01, analytic, significant=2)
    np.testing.assert_approx_equal(dice, 2 * volume_01 / (volume_0 + volume_1), significant=10)