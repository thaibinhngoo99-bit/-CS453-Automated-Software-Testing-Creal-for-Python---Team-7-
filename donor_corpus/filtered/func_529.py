@main.command()
def subscribe_changelog():
    changelog_url = CONFIG.root_url.rstrip('/') + '/changelog.atom'
    feed = Feed.objects.get(url=changelog_url)
    if not feed:
        click.echo(f'not found changelog feed url={changelog_url}')
        return
    click.echo(f'changelog feed {feed}')
    User = get_user_model()
    users = list(User.objects.all())
    click.echo(f'total {len(users)} users')
    for user in tqdm.tqdm(users, ncols=80, ascii=True):
        with transaction.atomic():
            user_feed = UserFeed.objects.filter(user_id=user.id, feed_id=feed.id).first()
            if not user_feed:
                user_feed = UserFeed(user_id=user.id, feed_id=feed.id, is_from_bookmark=False)
                user_feed.save()