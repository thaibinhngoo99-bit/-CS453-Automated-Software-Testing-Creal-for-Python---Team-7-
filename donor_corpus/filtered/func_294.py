def convert(input, output, single_file=False):
    """
    Run dcm2niix on input file
    """
    dirname = os.path.dirname(output)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    basename = os.path.basename(output)
    basename = re.sub('.nii(.gz)?', '', basename)
    dcm2niix = commons.which('dcm2niix')
    cmd = ['dcm2niix']
    if single_file:
        cmd.extend(['-s', 'y'])
    cmd.extend(['-b', 'y', '-z', 'y', '-f', basename, '-o', dirname, input])
    logger.debug(cmd)
    sp.check_output(cmd)