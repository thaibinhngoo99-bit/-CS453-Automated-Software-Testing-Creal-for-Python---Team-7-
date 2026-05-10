@main.command()
@click.option('--feeds', help="feed ids, separate by ','")
@click.option('--union-feeds', help="union feed ids, separate by ','")
@click.option('--key', help='feed url or title keyword')
@click.option('--expire', type=int, default=1, help='expire hours')
def refresh_feed(feeds, union_feeds, key, expire=None):
    feed_ids = []
    if feeds:
        feed_ids.extend(_get_feed_ids(feeds))
    if union_feeds:
        feed_ids.extend(_decode_union_feed_ids(union_feeds))
    if key:
        cond = Q(url__contains=key) | Q(title__contains=key)
        feed_objs = Feed.objects.filter(cond).only('id').all()
        feed_ids.extend((x.id for x in feed_objs))
    feed_ids = list(sorted(set(feed_ids)))
    expire_at = time.time() + expire * 60 * 60
    for feed_id in tqdm.tqdm(feed_ids, ncols=80, ascii=True):
        feed = Feed.objects.only('id', 'url', 'use_proxy').get(pk=feed_id)
        scheduler.tell('worker_rss.sync_feed', dict(feed_id=feed.id, url=feed.url, use_proxy=feed.use_proxy, is_refresh=True), expire_at=expire_at)