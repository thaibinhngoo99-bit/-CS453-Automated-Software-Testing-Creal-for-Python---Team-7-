def test_bg_swap_fast():
    """
    Fast test for background swap.
    """
    bg_x = np.ones(shape=[2, 5, 5, 3]) * -1
    bg_y = np.random.rand(2)
    fg = np.random.normal(loc=0.5, scale=0.1, size=[5, 5])
    bg = InMemoryDataset(bg_x, bg_y)
    bg_swap = BackgroundSwap(bg, input_dim=(5, 5), normalize_bg=None)
    spliced_1_channel = bg_swap(fg)[:, :, 0]
    assert np.array_equal(spliced_1_channel <= -1, fg <= 0.5)