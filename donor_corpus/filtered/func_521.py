@main.command()
@click.option('--feeds', help="feed ids, separate by ','")
def update_feed_dryness(feeds=None):
    feed_ids = _get_feed_ids(feeds)
    LOG.info('total %s feeds', len(feed_ids))
    for feed_id in tqdm.tqdm(feed_ids, ncols=80, ascii=True):
        with transaction.atomic():
            feed = Feed.get_by_pk(feed_id)
            if feed.total_storys <= 0:
                continue
            cnt = feed.monthly_story_count
            if not cnt:
                Story.refresh_feed_monthly_story_count(feed_id)
            feed.refresh_from_db()
            feed.dryness = feed.monthly_story_count.dryness()
            feed.save()