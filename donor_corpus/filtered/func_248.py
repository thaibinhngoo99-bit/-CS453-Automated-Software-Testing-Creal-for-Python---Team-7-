def add_header(vgg, extra_layers, boxes_per_location, num_classes):
    regression_headers = []
    classification_headers = []
    vgg_source = [21, -2]
    for k, v in enumerate(vgg_source):
        regression_headers += [nn.Conv2d(vgg[v].out_channels, boxes_per_location[k] * 4, kernel_size=3, padding=1)]
        classification_headers += [nn.Conv2d(vgg[v].out_channels, boxes_per_location[k] * num_classes, kernel_size=3, padding=1)]
    for k, v in enumerate(extra_layers[1::2], 2):
        regression_headers += [nn.Conv2d(v.out_channels, boxes_per_location[k] * 4, kernel_size=3, padding=1)]
        classification_headers += [nn.Conv2d(v.out_channels, boxes_per_location[k] * num_classes, kernel_size=3, padding=1)]
    return (regression_headers, classification_headers)