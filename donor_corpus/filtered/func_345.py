def get_keywords():
    """Get the keywords needed to look up the version information."""
    git_refnames = '$Format:%d$'
    git_full = '$Format:%H$'
    git_date = '$Format:%ci$'
    keywords = {'refnames': git_refnames, 'full': git_full, 'date': git_date}
    return keywords