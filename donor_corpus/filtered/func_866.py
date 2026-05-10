def load_spline_params():
    dirname = os.path.dirname(__file__)
    with open(os.path.join(dirname, '../misc/partition_spline.npz'), 'rb') as spline_file:
        with np.load(spline_file, allow_pickle=False) as f:
            spline_x_scale = torch.tensor(f['x_scale'])
            spline_values = torch.tensor(f['values'])
            spline_tangents = torch.tensor(f['tangents'])
    return (spline_x_scale, spline_values, spline_tangents)