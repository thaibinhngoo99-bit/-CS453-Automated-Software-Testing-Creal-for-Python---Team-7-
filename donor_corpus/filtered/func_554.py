def fcn(parameters):
    x = parameters['x'].value
    y = parameters['y'].value
    z = parameters['z'].value
    x_opt, y_opt, z_opt = (2, 300000.0, 4e-05)
    x_err, y_err, z_err = (0.2, 30000.0, 4e-06)
    return ((x - x_opt) / x_err) ** 2 + ((y - y_opt) / y_err) ** 2 + ((z - z_opt) / z_err) ** 2