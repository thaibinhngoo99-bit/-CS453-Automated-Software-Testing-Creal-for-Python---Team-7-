def _add_changes(ret, changes_old, changes_new, comments):
    ret['comment'] = ',\n'.join(comments)
    if changes_old:
        ret['changes']['old'] = changes_old
    if changes_new:
        ret['changes']['new'] = changes_new