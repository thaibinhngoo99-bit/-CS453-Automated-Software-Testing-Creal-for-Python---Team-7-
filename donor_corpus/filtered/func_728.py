def delete_current_music():
    print('delete current music')
    current = r.get_current()
    if not current:
        print('Nothing is running, bailing out')
        return
    delete_remote_file(current)
    play_next()