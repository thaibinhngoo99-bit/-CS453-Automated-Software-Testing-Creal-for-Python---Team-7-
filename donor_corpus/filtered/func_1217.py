def package_info(image):
    """Returns the commands used to update system repositories, install
    system packages and clean afterwards.

    Args:
        image (str): image to be used at run-time. Should be of the form
            <image_name>:<image_tag> e.g. "ubuntu:18.04"

    Returns:
        A tuple of (update, install, clean) commands.
    """
    image_data = data()[image]
    update = image_data['update']
    install = image_data['install']
    clean = image_data['clean']
    return (update, install, clean)