@main.command()
def update_story_is_user_marked():
    user_storys = list(UserStory.objects.exclude(is_watched=False, is_favorited=False).all())
    LOG.info('total %s user marked storys', len(user_storys))
    if not user_storys:
        return
    for user_story in tqdm.tqdm(user_storys, ncols=80, ascii=True):
        Story.set_user_marked_by_id(user_story.story_id)