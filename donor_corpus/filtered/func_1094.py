def main():
    print('starting...', end='')
    state = True
    print('[' + ('OK' if state else 'ERROR') + ']')
    winThread.start()
    comunication.start()