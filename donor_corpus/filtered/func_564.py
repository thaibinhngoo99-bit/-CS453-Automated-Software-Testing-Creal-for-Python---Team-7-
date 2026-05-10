@pytest.mark.level0
@pytest.mark.platform_x86_gpu_training
@pytest.mark.env_onecard
def tanh_grad_grad_base(dtype, loss):
    np.random.seed(1)
    shape = (4, 2)
    y_np = (np.random.rand(*shape) * 2 - 1).astype(dtype)
    grad_np = (np.random.rand(*shape) * 20 - 10).astype(dtype)
    dout_np = (np.random.rand(*shape) * 20 - 10).astype(dtype)
    y_np_32 = y_np.astype(np.float32)
    grad_np_32 = grad_np.astype(np.float32)
    dout_np_32 = dout_np.astype(np.float32)
    dy_np = (dout_np_32 * grad_np_32 * -2.0 * y_np_32).astype(dtype)
    dgrad_np = (dout_np_32 * (1 - y_np_32 * y_np_32)).astype(dtype)
    y_ms = Tensor(y_np)
    grad_ms = Tensor(grad_np)
    dout_ms = Tensor(dout_np)
    forward_net = NetTanhGrad()
    net = NetTanhGradGrad(forward_net)
    dy_ms, dgrad_ms = net(y_ms, grad_ms, dout_ms)
    assert np.allclose(dy_ms.asnumpy(), dy_np, loss, loss)
    assert np.allclose(dgrad_ms.asnumpy(), dgrad_np, loss, loss)