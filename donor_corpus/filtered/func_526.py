@main.command()
@click.option('--storys', help="story ids, separate by ','")
def update_story_images(storys=None):
    story_ids = _get_story_ids(storys)
    LOG.info('total %s storys', len(story_ids))
    for story_id in tqdm.tqdm(story_ids, ncols=80, ascii=True):
        story = Story.objects.get(pk=story_id)
        scheduler.tell('harbor_rss.update_story_images', dict(story_id=story_id, story_url=story.link, images=[]))