@main.command()
def update_feed_use_proxy():
    if not CONFIG.rss_proxy_enable:
        click.echo('rss proxy not enable!')
        return
    blacklist = ['%博客园%', '%微信%', '%新浪%', '%的评论%', '%Comments on%']
    sql = "\n    select * from rssant_api_feed\n    where (NOT title LIKE ANY(%s)) AND (\n        dt_created >= '2020-04-01' or\n        (total_storys <= 5 and dt_updated <= '2019-12-01')\n    )\n    "
    feeds = list(Feed.objects.raw(sql, [blacklist]))
    click.echo(f'{len(feeds)} feeds need check')
    reader = FeedReader(**_proxy_helper.get_proxy_options())
    proxy_feeds = []
    with reader:
        for i, feed in enumerate(feeds):
            click.echo(f'#{i} {feed}')
            status = reader.read(feed.url).status
            click.echo(f'    #{i} status={FeedResponseStatus.name_of(status)}')
            if FeedResponseStatus.is_need_proxy(status):
                proxy_status = reader.read(feed.url, use_proxy=True).status
                click.echo(f'    #{i} proxy_status={FeedResponseStatus.name_of(proxy_status)}')
                if proxy_status == 200:
                    proxy_feeds.append(feed)
    click.echo(f'{len(proxy_feeds)} feeds need use proxy')
    if proxy_feeds:
        with transaction.atomic():
            for feed in tqdm.tqdm(proxy_feeds, ncols=80, ascii=True):
                feed.refresh_from_db()
                feed.use_proxy = True
                feed.save()