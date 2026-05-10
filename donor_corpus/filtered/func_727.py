def play_radio():
    if r.get_current().get('file', '') == 'http://ice.somafm.com/groovesalad':
        print('will not skip own sender')
        return
    print('playing radio')
    tell_gobbelz('Starting Radio Stream')
    r.add_song('http://ice.somafm.com/groovesalad')
    r.play_last()