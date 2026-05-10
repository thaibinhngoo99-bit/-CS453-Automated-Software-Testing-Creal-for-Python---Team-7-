@main.command()
def fix_user_story_offset():
    sql = '\n    SELECT us.id, us."offset", story."offset"\n    FROM rssant_api_userstory AS us\n    LEFT OUTER JOIN rssant_api_story AS story\n        ON us.story_id=story.id\n    WHERE us."offset" != story."offset"\n    '
    items = []
    with connection.cursor() as cursor:
        cursor.execute(sql)
        for us_id, us_offset, story_offset in cursor.fetchall():
            items.append((us_id, us_offset, story_offset))
    click.echo(f'total {len(items)} mismatch user story offset')
    if not items:
        return
    with transaction.atomic():
        for us_id, us_offset, story_offset in tqdm.tqdm(items, ncols=80, ascii=True):
            UserStory.objects.filter(pk=us_id).update(offset=-us_offset)
        for us_id, us_offset, story_offset in tqdm.tqdm(items, ncols=80, ascii=True):
            UserStory.objects.filter(pk=us_id).update(offset=story_offset)