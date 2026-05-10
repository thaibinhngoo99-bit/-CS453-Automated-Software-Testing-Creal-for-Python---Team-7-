def init_command_line(argv):
    from argparse import ArgumentParser
    usage = 'seq2seq'
    description = ArgumentParser(usage)
    description.add_argument('--w2v_path', type=str, default='/users3/yfwang/data/w2v/opensubtitle/')
    description.add_argument('--corpus_path', type=str, default='/users3/yfwang/data/corpus/opensubtitle/')
    description.add_argument('--w2v', type=str, default='train_all_200e.w2v')
    description.add_argument('--test_file', type=str, default='test_sessions.txt')
    description.add_argument('--max_context_size', type=int, default=2)
    description.add_argument('--batch_size', type=int, default=64)
    description.add_argument('--enc_hidden_size', type=int, default=512)
    description.add_argument('--max_senten_len', type=int, default=15)
    description.add_argument('--dropout', type=float, default=0.5)
    description.add_argument('--teach_forcing', type=int, default=1)
    description.add_argument('--print_every', type=int, default=100, help='print every batches when training')
    description.add_argument('--weights', type=str, default=None)
    return description.parse_args(argv)