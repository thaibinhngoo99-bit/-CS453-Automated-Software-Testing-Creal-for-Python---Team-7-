def run_cmd(command: str):
    """run_cmd Run given shell command
    Args:
        command (str): Shell command to run
    Returns:
        (int, str): Status code, stdout of shell command
    Examples:
        >>> run_cmd("ls /")
        (0, 'bin
boot
dev
etc
home
init
lib
lib32
lib64
libx32
lost+found
media
mnt
opt
proc
root
run
sbin
snap
srv
sys
tmp
usr
var
')
    """
    command = f'{os.getenv('SHELL')} -c "{command}"'
    pipe = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout = ''
    if pipe.stdout is not None:
        stdout = ''.join([line.decode('utf-8') for line in iter(pipe.stdout.readline, b'')])
        pipe.stdout.close()
    returncode = pipe.wait()
    print(stdout)
    return (returncode, stdout)