def debug(rank, world_size, tensor, dp, noise_multiplier=0, max_grad_norm=100000000.0):
    local_rank = setup_and_get_device(rank, world_size)
    print(f'Rank: {rank},World size: {world_size}, local_rank: {local_rank}')
    tensor = tensor.to(local_rank)
    print(f'dp: {dp}')
    print(tensor)
    cleanup()