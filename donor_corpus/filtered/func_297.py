@main.route('/sources/<id>')
def articles(id):
    """
	view articles page
	"""
    articles = get_articles(id)
    title = f'NH | {id}'
    return render_template('articles.html', title=title, articles=articles)