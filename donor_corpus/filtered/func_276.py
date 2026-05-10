def main1():
    timestamp_file = sys.argv[1]
    segments = read_split_tsv(timestamp_file)
    for i, segment in enumerate(segments):
        inmp4 = input_video(segment)
        outmp4 = out_video(segment, greek=True)
        timestamps = manage_timestamps(segment)
        to_cut_yaml(inmp4, outmp4, f'{i}.yml', timestamps)