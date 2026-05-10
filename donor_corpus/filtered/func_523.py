@main.command()
@click.option('--storys', help="story ids, separate by ','")
def update_story_has_mathjax(storys=None):
    story_ids = _get_story_ids(storys)
    LOG.info('total %s storys', len(story_ids))
    for story_id in tqdm.tqdm(story_ids, ncols=80, ascii=True):
        with transaction.atomic():
            story = Story.objects.only('id', 'content', '_version').get(pk=story_id)
            if processor.story_has_mathjax(story.content):
                story.has_mathjax = True
                story.save()