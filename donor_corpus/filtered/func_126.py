def main():
    parser = get_parser()
    args = parser.parse_args()
    fscps = [io.open(scp, 'r', encoding='utf-8') for scp in args.scp]
    for linenum, lines in enumerate(zip_longest(*fscps)):
        keys = []
        wavs = []
        for line, scp in zip(lines, args.scp):
            if line is None:
                raise RuntimeError('Numbers of line mismatch')
            sps = line.split(' ', 1)
            if len(sps) != 2:
                raise RuntimeError('Invalid line is found: {}, line {}: "{}" '.format(scp, linenum, line))
            key, wav = sps
            keys.append(key)
            wavs.append(wav.strip())
        if not all((k == keys[0] for k in keys)):
            raise RuntimeError('The ids mismatch. Hint; the input files must be sorted and must have same ids: {}'.format(keys))
        args.out.write('{} sox -M {} -c {} -t wav - |\n'.format(keys[0], ' '.join(('{}'.format(w) for w in wavs)), len(fscps)))