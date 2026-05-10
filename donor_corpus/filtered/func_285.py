@click.command(cls=CmdsLoader)
@click.option('-v', '--verbose', count=True, help='Explain what is being done')
@click.option('-i', '--interactive', count=True, help='Show all the output from the established remote shell session')
@click.option('-f', '--force', is_flag=True, help='Force the execution of the commands if one fails')
@click.option('-h', '--host', default='myserver', help='The name of the connection defined in ~/.ssh/config file')
@click.pass_context
def yoda(ctx, verbose, interactive, force, host):
    shell = Shell(host)
    hostConfig = importHost(host)
    shell.setConfig(hostConfig[0]['options'])
    shell.connect()
    if verbose:
        click.echo('Connected to host %s' % host)
    shell.interactive = bool(interactive)
    shell.force = force
    cmd = Cmd()
    cmd.shell = shell
    cmd.host = host
    cmd.verbose = verbose
    ctx.obj = cmd