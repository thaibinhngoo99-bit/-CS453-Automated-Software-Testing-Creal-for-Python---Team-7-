def build_info(image, spack_version):
    """Returns the name of the build image and its tag.

    Args:
        image (str): image to be used at run-time. Should be of the form
            <image_name>:<image_tag> e.g. "ubuntu:18.04"
        spack_version (str): version of Spack that we want to use to build

    Returns:
        A tuple with (image_name, image_tag) for the build image
    """
    image_data = data()[image]
    build_image = image_data['build']
    try:
        build_tag = image_data['build_tags'].get(spack_version, spack_version)
    except KeyError:
        msg = 'the image "{0}" has no tag for Spack version "{1}" [valid versions are {2}]'
        msg = msg.format(build_image, spack_version, ', '.join(image_data['build_tags'].keys()))
        raise ValueError(msg)
    return (build_image, build_tag)