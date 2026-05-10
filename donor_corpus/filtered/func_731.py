def parse_args():
    """
  Parse input arguments
  """
    parser = argparse.ArgumentParser(description='Train a Fast R-CNN network')
    parser.add_argument('--dataset', dest='dataset', help='training dataset', default='pascal_voc', type=str)
    parser.add_argument('--cfg', dest='cfg_file', help='optional config file', default='cfgs/vgg16.yml', type=str)
    parser.add_argument('--net', dest='net', help='vgg16, res50, res101, res152', default='res101', type=str)
    parser.add_argument('--set', dest='set_cfgs', help='set config keys', default=None, nargs=argparse.REMAINDER)
    parser.add_argument('--load_dir', dest='load_dir', help='directory to load models', default='models', type=str)
    parser.add_argument('--cuda', dest='cuda', help='whether use CUDA', action='store_true')
    parser.add_argument('--ls', dest='large_scale', help='whether use large imag scale', action='store_true')
    parser.add_argument('--mGPUs', dest='mGPUs', help='whether use multiple GPUs', action='store_true')
    parser.add_argument('--cag', dest='class_agnostic', help='whether perform class_agnostic bbox regression', action='store_true')
    parser.add_argument('--parallel_type', dest='parallel_type', help='which part of model to parallel, 0: all, 1: model before roi pooling', default=0, type=int)
    parser.add_argument('--checksession', dest='checksession', help='checksession to load model', default=1, type=int)
    parser.add_argument('--checkepoch', dest='checkepoch', help='checkepoch to load network', default=1, type=int)
    parser.add_argument('--checkpoint', dest='checkpoint', help='checkpoint to load network', default=10021, type=int)
    parser.add_argument('--vis', dest='vis', help='visualization mode', action='store_true')
    parser.add_argument('--input_dir', dest='input_dir', help='directory to save models', type=str)
    args = parser.parse_args()
    return args