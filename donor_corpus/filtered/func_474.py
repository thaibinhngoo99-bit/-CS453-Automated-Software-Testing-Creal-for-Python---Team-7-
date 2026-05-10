def test_overlapping_bounds():
    radius_0 = 10.0
    radius_1 = 7.0
    centre_1 = 5.0
    radius_2 = 4.0
    centre_2 = 15.0
    radius_3 = 4.0
    centre_3 = 0.0
    sphere_0 = vtk.vtkSphereSource()
    sphere_0.SetRadius(radius_0)
    sphere_0.SetPhiResolution(12)
    sphere_0.SetThetaResolution(12)
    sphere_0.SetCenter(0.0, 0.0, 0.0)
    sphere_0.Update()
    vtk_model_0 = sphere_0.GetOutput()
    sphere_1 = vtk.vtkSphereSource()
    sphere_1.SetRadius(radius_1)
    sphere_1.SetPhiResolution(12)
    sphere_1.SetThetaResolution(21)
    sphere_1.SetCenter(centre_1, 0.0, 0.0)
    sphere_1.Update()
    vtk_model_1 = sphere_1.GetOutput()
    sphere_2 = vtk.vtkSphereSource()
    sphere_2.SetRadius(radius_2)
    sphere_2.SetPhiResolution(12)
    sphere_2.SetThetaResolution(21)
    sphere_2.SetCenter(centre_2, 0.0, 0.0)
    sphere_2.Update()
    vtk_model_2 = sphere_2.GetOutput()
    sphere_3 = vtk.vtkSphereSource()
    sphere_3.SetRadius(radius_3)
    sphere_3.SetPhiResolution(12)
    sphere_3.SetThetaResolution(21)
    sphere_3.SetCenter(centre_3, 0.0, 0.0)
    sphere_3.Update()
    vtk_model_3 = sphere_3.GetOutput()
    assert pdu.check_overlapping_bounds(vtk_model_0, vtk_model_1)
    assert pdu.check_overlapping_bounds(vtk_model_1, vtk_model_0)
    assert not pdu.check_overlapping_bounds(vtk_model_0, vtk_model_2)
    assert not pdu.check_overlapping_bounds(vtk_model_2, vtk_model_0)
    assert pdu.check_overlapping_bounds(vtk_model_0, vtk_model_3)
    assert pdu.check_overlapping_bounds(vtk_model_3, vtk_model_0)