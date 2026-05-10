def print_usage():
    quality_runner_types = ['VMAF', 'PSNR', 'SSIM', 'MS_SSIM']
    print('usage: ' + os.path.basename(sys.argv[0]) + ' quality_type dataset_filepath\n')
    print('quality_type:\n\t' + '\n\t'.join(quality_runner_types) + '\n')