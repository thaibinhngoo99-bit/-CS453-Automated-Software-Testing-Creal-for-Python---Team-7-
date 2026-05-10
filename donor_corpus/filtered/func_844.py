@pytest.mark.slow
def test_background_swap_numpy():
    """
    Test background swap on a single ndarray input.
    """
    mnist = MNIST(DATA_PATH, download=True, train=True)
    cifar = CIFAR10(DATA_PATH, download=True, train=True)
    bg_swap = BackgroundSwap(cifar, input_dim=(28, 28))
    im = mnist.get_data()[0][0]
    im = bg_swap(im)