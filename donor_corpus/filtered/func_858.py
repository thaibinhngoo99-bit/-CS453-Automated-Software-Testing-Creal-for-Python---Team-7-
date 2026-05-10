def setup_and_get_device(rank, world_size, nonce=0):
    """
    Initialize the torch.distributed process group.
    If you run multiple groups in parallel or if you have zombie processes, you can add a nonce to avoid errors.
    """
    device = 0
    if sys.platform == 'win32':
        init_method = 'file:///{your local file path}'
        dist.init_process_group('gloo', init_method=init_method, rank=rank, world_size=world_size)
        device = rank
    elif os.environ.get('SLURM_NTASKS') is not None:
        os.environ['MASTER_ADDR'] = '127.0.0.1'
        os.environ['MASTER_PORT'] = str(7440 + nonce)
        local_rank = int(os.environ.get('SLURM_LOCALID'))
        dist.init_process_group(backend='gloo', rank=rank, world_size=world_size)
        device = local_rank
    else:
        os.environ['MASTER_ADDR'] = 'localhost'
        os.environ['MASTER_PORT'] = '12355'
        os.environ['RANK'] = str(rank)
        os.environ['WORLD_SIZE'] = str(world_size)
        dist.init_process_group(init_method='env://', backend='nccl')
        device = rank
    return device