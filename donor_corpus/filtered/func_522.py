@main.command()
@click.option('--feeds', help="feed ids, separate by ','")
def update_feed_dt_first_story_published(feeds=None):
    feed_ids = _get_feed_ids(feeds)
    LOG.info('total %s feeds', len(feed_ids))
    for feed_id in tqdm.tqdm(feed_ids, ncols=80, ascii=True):
        with transaction.atomic():
            feed = Feed.get_by_pk(feed_id)
            if feed.dt_first_story_published:
                continue
            if feed.total_storys <= 0:
                continue
            try:
                story = Story.get_by_offset(feed_id, 0, detail=True)
            except Story.DoesNotExist:
                LOG.warning(f'story feed_id={feed_id} offset=0 not exists')
                continue
            feed.dt_first_story_published = story.dt_published
            feed.save()