@main.command()
@click.option('--feeds', help="feed ids, separate by ','")
def update_feed_monthly_story_count(feeds=None):
    feed_ids = _get_feed_ids(feeds)
    LOG.info('total %s feeds', len(feed_ids))
    for feed_id in tqdm.tqdm(feed_ids, ncols=80, ascii=True):
        with transaction.atomic():
            Story.refresh_feed_monthly_story_count(feed_id)