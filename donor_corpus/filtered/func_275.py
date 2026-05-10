def main():
    timestamp_file = sys.argv[1]
    segments = read_split_tsv(timestamp_file)
    for segment in segments:
        inmp4 = input_video(segment)
        outmp4 = 'out/' + out_video(segment, greek=True)
        timestamps = manage_timestamps(segment)
        timestamp_args = format_timestamp_args(timestamps)
        ffmpeg(inmp4, outmp4, timestamp_args)