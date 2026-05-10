def extract_frame(movie_files_dir, out_dir):
    movie_files = glob.glob(movie_files_dir)
    if not movie_files:
        print('movie files are not found.')
        return
    for movie_file in movie_files:
        ext = movie_file.split('.')[-1]
        if not ext == 'mp4' or not ext == 'MP4':
            print(f"can't extract this movie file: {movie_file}")
            continue
        out_dir = out_dir
        if not os.path.exists(out_dir):
            os.mkdir(out_dir)
        cap = cv2.VideoCapture(movie_file)
        if not cap.isOpened():
            print(f"can't extract this movie file: {movie_file}")
            return
        digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))
        n = 0
        while True:
            ret, frame = cap.read()
            if ret:
                cv2.imwrite(f'{movie_file}_{str(n).zfill(digit)}.jpg', frame)
                n += 1
                continue
            return
    print(f'{len(movie_files)} movie files extracted')