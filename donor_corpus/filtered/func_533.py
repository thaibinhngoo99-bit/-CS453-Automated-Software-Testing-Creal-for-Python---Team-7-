@main.command()
@click.option('--dst', required=True, help='actor dst')
@click.option('--content', help='message content')
@click.option('--expire-seconds', type=int, help='expire time in seconds')
def tell(dst, content, expire_seconds):
    if content:
        content = json.loads(content)
    expire_at = None
    if expire_seconds:
        expire_at = int(time.time()) + expire_seconds
    scheduler.tell(dst, content=content, expire_at=expire_at)