@pytest.mark.slow
def test_background_tranformation():
    """
    Example code using TransformationIncremental to create a setting with 3 tasks.
    """
    cifar = CIFAR10(DATA_PATH, train=True)
    mnist = MNIST(DATA_PATH, download=False, train=True)
    nb_task = 3
    list_trsf = []
    for i in range(nb_task):
        list_trsf.append([torchvision.transforms.ToTensor(), BackgroundSwap(cifar, bg_label=i, input_dim=(28, 28)), torchvision.transforms.ToPILImage()])
    scenario = TransformationIncremental(mnist, base_transformations=[torchvision.transforms.ToTensor()], incremental_transformations=list_trsf)
    folder = 'tests/samples/background_trsf/'
    if not os.path.exists(folder):
        os.makedirs(folder)
    for task_id, task_data in enumerate(scenario):
        task_data.plot(path=folder, title=f'background_{task_id}.jpg', nb_samples=100, shape=[28, 28, 3])
        loader = DataLoader(task_data)
        _, _, _ = next(iter(loader))