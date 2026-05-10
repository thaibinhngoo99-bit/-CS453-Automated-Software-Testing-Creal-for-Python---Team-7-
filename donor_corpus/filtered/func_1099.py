def get_response(gtpStream):
    succeeded = False
    result = ''
    while succeeded == False:
        line = gtpStream.stdout.readline()
        if line[0] == '=':
            succeeded = True
            line = line.strip()
            print('Response is: ' + line)
            result = re.sub('^= ?', '', line)
    return result