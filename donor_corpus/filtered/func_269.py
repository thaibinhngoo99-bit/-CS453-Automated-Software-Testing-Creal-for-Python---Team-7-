def out_video(segment, greek=True):
    title_idx = 3 if greek else 4
    title, topic, subtopic = (segment[title_idx], segment[1], segment[2])
    name = f'{title}_{topic}-{subtopic}.mp4'
    return name