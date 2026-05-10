@main.command()
@click.option('--dry-run', is_flag=True)
def fix_feed_total_storys(dry_run=False):
    incorrect_feeds = Story.query_feed_incorrect_total_storys()
    LOG.info('total %s incorrect feeds', len(incorrect_feeds))
    header = ['feed_id', 'total_storys', 'correct_total_storys']
    click.echo(format_table(incorrect_feeds, header=header))
    if dry_run:
        return
    with transaction.atomic():
        num_corrected = 0
        for feed_id, *__ in tqdm.tqdm(incorrect_feeds, ncols=80, ascii=True):
            fixed = Story.fix_feed_total_storys(feed_id)
            if fixed:
                num_corrected += 1
        LOG.info('correct %s feeds', num_corrected)