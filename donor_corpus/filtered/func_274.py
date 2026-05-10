def ffmpeg(inp, out, timestamps_args):
    if len(timestamps_args) == 1:
        run_cmd(f"ffmpeg -y -i '{inp}' " + timestamps_args[0] + f" -c:v h265_nvenc -crf 24 -preset fast -c:a copy '{out}'")
        return
    mp4s = []
    for i, arg in enumerate(timestamps_args):
        mp4s.append(f'{i}.mp4')
        cmd = f"ffmpeg  -i '{inp}' " + arg + f" -c:v h265_nvenc -crf 24 -preset fast -c:a copy '{i}.mp4'"
        print(cmd)
        run_cmd(cmd)
    tmp = '.tmp_files.txt'
    with open(tmp, 'w') as fd:
        for f in mp4s:
            fd.write(f"file '{f}'\n")
    run_cmd(f"ffmpeg -y -f concat -i .tmp_files.txt '{out}'")
    run_cmd(f'rm {tmp} ' + ' '.join(mp4s))