def get(filepath):
    """
    Return (width, height) for a given img file content
    no requirements
    :type filepath: Union[bytes, str, pathlib.Path]
    :rtype Tuple[int, int]
    """
    height = -1
    width = -1
    if isinstance(filepath, io.BytesIO):
        fhandle = filepath
    else:
        fhandle = open(filepath, 'rb')
    try:
        head = fhandle.read(24)
        size = len(head)
        if size >= 10 and head[:6] in (b'GIF87a', b'GIF89a'):
            try:
                width, height = struct.unpack('<hh', head[6:10])
            except struct.error:
                raise ValueError('Invalid GIF file')
        elif size >= 24 and head.startswith(b'\x89PNG\r\n\x1a\n') and (head[12:16] == b'IHDR'):
            try:
                width, height = struct.unpack('>LL', head[16:24])
            except struct.error:
                raise ValueError('Invalid PNG file')
        elif size >= 16 and head.startswith(b'\x89PNG\r\n\x1a\n'):
            try:
                width, height = struct.unpack('>LL', head[8:16])
            except struct.error:
                raise ValueError('Invalid PNG file')
        elif size >= 2 and head.startswith(b'\xff\xd8'):
            try:
                fhandle.seek(0)
                size = 2
                ftype = 0
                while not 192 <= ftype <= 207 or ftype in [196, 200, 204]:
                    fhandle.seek(size, 1)
                    byte = fhandle.read(1)
                    while ord(byte) == 255:
                        byte = fhandle.read(1)
                    ftype = ord(byte)
                    size = struct.unpack('>H', fhandle.read(2))[0] - 2
                fhandle.seek(1, 1)
                height, width = struct.unpack('>HH', fhandle.read(4))
            except (struct.error, TypeError):
                raise ValueError('Invalid JPEG file')
        elif size >= 12 and head.startswith(b'\x00\x00\x00\x0cjP  \r\n\x87\n'):
            fhandle.seek(48)
            try:
                height, width = struct.unpack('>LL', fhandle.read(8))
            except struct.error:
                raise ValueError('Invalid JPEG2000 file')
        elif size >= 8 and head.startswith(b'MM\x00*'):
            offset = struct.unpack('>L', head[4:8])[0]
            fhandle.seek(offset)
            ifdsize = struct.unpack('>H', fhandle.read(2))[0]
            for i in range(ifdsize):
                tag, datatype, count, data = struct.unpack('>HHLL', fhandle.read(12))
                if tag == 256:
                    if datatype == 3:
                        width = int(data / 65536)
                    elif datatype == 4:
                        width = data
                    else:
                        raise ValueError('Invalid TIFF file: width column data type should be SHORT/LONG.')
                elif tag == 257:
                    if datatype == 3:
                        height = int(data / 65536)
                    elif datatype == 4:
                        height = data
                    else:
                        raise ValueError('Invalid TIFF file: height column data type should be SHORT/LONG.')
                if width != -1 and height != -1:
                    break
            if width == -1 or height == -1:
                raise ValueError('Invalid TIFF file: width and/or height IDS entries are missing.')
        elif size >= 8 and head.startswith(b'II*\x00'):
            offset = struct.unpack('<L', head[4:8])[0]
            fhandle.seek(offset)
            ifdsize = struct.unpack('<H', fhandle.read(2))[0]
            for i in range(ifdsize):
                tag, datatype, count, data = struct.unpack('<HHLL', fhandle.read(12))
                if tag == 256:
                    width = data
                elif tag == 257:
                    height = data
                if width != -1 and height != -1:
                    break
            if width == -1 or height == -1:
                raise ValueError('Invalid TIFF file: width and/or height IDS entries are missing.')
        elif size >= 8 and head.startswith(b'II+\x00'):
            bytesize_offset = struct.unpack('<L', head[4:8])[0]
            if bytesize_offset != 8:
                raise ValueError('Invalid BigTIFF file: Expected offset to be 8, found {} instead.'.format(offset))
            offset = struct.unpack('<Q', head[8:16])[0]
            fhandle.seek(offset)
            ifdsize = struct.unpack('<Q', fhandle.read(8))[0]
            for i in range(ifdsize):
                tag, datatype, count, data = struct.unpack('<HHQQ', fhandle.read(20))
                if tag == 256:
                    width = data
                elif tag == 257:
                    height = data
                if width != -1 and height != -1:
                    break
            if width == -1 or height == -1:
                raise ValueError('Invalid BigTIFF file: width and/or height IDS entries are missing.')
        elif size >= 5 and (head.startswith(b'<?xml') or head.startswith(b'<svg')):
            fhandle.seek(0)
            data = fhandle.read(1024)
            try:
                data = data.decode('utf-8')
                width = re.search('[^-]width="(.*?)"', data).group(1)
                height = re.search('[^-]height="(.*?)"', data).group(1)
            except Exception:
                raise ValueError('Invalid SVG file')
            width = _convertToPx(width)
            height = _convertToPx(height)
        elif head[:1] == b'P' and head[1:2] in b'123456':
            fhandle.seek(2)
            sizes = []
            while True:
                next_chr = fhandle.read(1)
                if next_chr.isspace():
                    continue
                if next_chr == b'':
                    raise ValueError('Invalid Netpbm file')
                if next_chr == b'#':
                    fhandle.readline()
                    continue
                if not next_chr.isdigit():
                    raise ValueError('Invalid character found on Netpbm file')
                size = next_chr
                next_chr = fhandle.read(1)
                while next_chr.isdigit():
                    size += next_chr
                    next_chr = fhandle.read(1)
                sizes.append(int(size))
                if len(sizes) == 2:
                    break
                fhandle.seek(-1, os.SEEK_CUR)
            width, height = sizes
    finally:
        fhandle.close()
    return (width, height)