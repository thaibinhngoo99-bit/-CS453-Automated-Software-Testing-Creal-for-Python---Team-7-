@pytest.mark.slow
def test_background_swap_torch():
    """
    Test background swap on a single tensor input.
    """
    cifar = CIFAR10(DATA_PATH, download=True, train=True)
    mnist = torchvision.datasets.MNIST(DATA_PATH, train=True, download=True, transform=torchvision.transforms.Compose([torchvision.transforms.ToTensor()]))
    bg_swap = BackgroundSwap(cifar, input_dim=(28, 28))
    im = mnist[0][0]
    im = bg_swap(im)