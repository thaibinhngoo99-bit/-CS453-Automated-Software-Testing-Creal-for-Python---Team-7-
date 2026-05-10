def get_transform(input_transforms_list):
    """
    Given the list of user specified transforms, return the
    torchvision.transforms.Compose() version of the transforms. Each transform
    in the composition is SSLTransformsWrapper which wraps the original
    transforms to handle multi-modal nature of input.
    """
    output_transforms = []
    for transform_config in input_transforms_list:
        transform = SSLTransformsWrapper.from_config(transform_config)
        output_transforms.append(transform)
    return pth_transforms.Compose(output_transforms)