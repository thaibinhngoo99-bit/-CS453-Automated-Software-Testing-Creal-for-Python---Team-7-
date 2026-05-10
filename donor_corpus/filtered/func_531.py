@main.command()
@click.argument('key')
def delete_feed(key):
    try:
        key = int(key)
    except ValueError:
        pass
    if isinstance(key, int):
        feed = Feed.get_by_pk(key)
    else:
        feed = Feed.objects.filter(Q(url__contains=key) | Q(title__contains=key)).first()
    if not feed:
        print(f'not found feed like {key}')
        return
    if click.confirm(f'delete {feed} ?'):
        feed.delete()