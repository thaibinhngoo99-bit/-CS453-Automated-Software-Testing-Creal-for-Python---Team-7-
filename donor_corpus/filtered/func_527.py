@main.command()
@click.option('--days', type=int, default=1)
@click.option('--limit', type=int, default=100)
@click.option('--threshold', type=int, default=99)
def delete_invalid_feeds(days=1, limit=100, threshold=99):
    sql = '\n    SELECT feed_id, title, link, url, status_code, count FROM (\n        SELECT feed_id, status_code, count(1) as count FROM rssant_api_rawfeed\n        WHERE dt_created >= %s and (status_code < 200 or status_code >= 400)\n        group by feed_id, status_code\n        having count(1) > 3\n        order by count desc\n        limit %s\n    ) error_feed\n    join rssant_api_feed\n        on error_feed.feed_id = rssant_api_feed.id\n    order by feed_id, status_code, count;\n    '
    sql_ok_count = '\n    SELECT feed_id, count(1) as count FROM rssant_api_rawfeed\n    WHERE dt_created >= %s and (status_code >= 200 and status_code < 400)\n        AND feed_id=ANY(%s)\n    group by feed_id\n    '
    t_begin = timezone.now() - timezone.timedelta(days=days)
    error_feeds = defaultdict(dict)
    with connection.cursor() as cursor:
        cursor.execute(sql, [t_begin, limit])
        for feed_id, title, link, url, status_code, count in cursor.fetchall():
            error_feeds[feed_id].update(feed_id=feed_id, title=title, link=link, url=url)
            error = error_feeds[feed_id].setdefault('error', {})
            error_name = FeedResponseStatus.name_of(status_code)
            error[error_name] = count
            error_feeds[feed_id]['error_count'] = sum(error.values())
            error_feeds[feed_id].update(ok_count=0, error_percent=100)
        cursor.execute(sql_ok_count, [t_begin, list(error_feeds)])
        for feed_id, ok_count in cursor.fetchall():
            feed = error_feeds[feed_id]
            total = feed['error_count'] + ok_count
            error_percent = round(feed['error_count'] / total * 100)
            feed.update(ok_count=ok_count, error_percent=error_percent)
    error_feeds = list(sorted(error_feeds.values(), key=lambda x: x['error_percent'], reverse=True))
    delete_feed_ids = []
    for feed in error_feeds:
        if feed['error_percent'] >= threshold:
            delete_feed_ids.append(feed['feed_id'])
            click.echo(pretty_format_json(feed))
    if delete_feed_ids:
        confirm_delete = click.confirm(f'Delete {len(delete_feed_ids)} feeds?')
        if not confirm_delete:
            click.echo('Abort!')
        else:
            UnionFeed.bulk_delete(delete_feed_ids)
            click.echo('Done!')
    return error_feeds