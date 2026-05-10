def main(argv):
    parser = argparse.ArgumentParser(description='XBox 360 NAND Flasher')
    parser.add_argument('port', metavar='port', type=str, help='serial port for comms (e.g. COM5 or /dev/ttyUSB0)')
    subparsers = parser.add_subparsers(title='Operations', dest='action')
    parser_read = subparsers.add_parser('read', help='Dumps an image from the NAND')
    parser_read.add_argument('file', nargs=1, type=argparse.FileType('wb'), help='The file to dump the NAND to')
    parser_read.add_argument('start', nargs='?', metavar='start', action='store', type=int, default=0, help='The block to start the action from')
    parser_read.add_argument('end', nargs='?', metavar='end', action='store', type=int, default=1024, help='The count of blocks to perform the action to')
    parser_write = subparsers.add_parser('write', help='Writes an image into the NAND')
    parser_write.add_argument('file', nargs=1, type=argparse.FileType('rb'), help='The image file to write to the NAND')
    parser_write.add_argument('start', nargs='?', metavar='start', action='store', type=int, default=0, help='The block to start the action from')
    parser_write.add_argument('end', nargs='?', metavar='end', action='store', type=int, default=1024, help='The count of blocks to perform the action to')
    arguments = parser.parse_args(argv[1:])
    ui = ConsoleUI()
    xf = XFlash(arguments.port)
    if arguments.action in ('erase', 'write', 'read'):
        try:
            flash_config = xf.flashInit()
            print('FlashConfig: 0x%08x' % flash_config)
            if flash_config <= 0:
                raise Exception('FlashConfig invalid!')
        except Exception as e:
            print('Error!', e)
            xf.flashDeInit()
            return 1
    try:
        if arguments.action == 'erase':
            start = arguments.start
            end = arguments.end
            ui.opStart('Erase')
            ui.opProgress(0, end)
            for b in range(start, end):
                status = xf.flashErase(b)
                ui.opProgress(b + 1, end)
            ui.opEnd('0x%04x blocks OK' % end)
        if arguments.action == 'read':
            start = arguments.start
            end = arguments.end
            ui.opStart('Read')
            ui.opProgress(0, end)
            for b in range(start, end):
                status, buffer = xf.flashReadBlock(b)
                ui.opProgress(b + 1, end)
                arguments.file[0].write(buffer)
        if arguments.action == 'write':
            start = arguments.start
            end = arguments.end
            blocksize = 528 * 32
            ui.opStart('Write')
            ui.opProgress(0, end)
            for b in range(start, end):
                buffer = arguments.file[0].read(blocksize)
                if len(buffer) < blocksize:
                    buffer += 'ÿ' * (blocksize - len(buffer))
                status = xf.flashWriteBlock(b, buffer)
                ui.opProgress(b + 1, end)
    except Exception as e:
        raise e
    finally:
        xf.flashDeInit()
        return 0