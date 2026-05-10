@main.route('/')
def index():
    """
	view root page function that returns the index the page and its data
	"""
    sources = get_sources('business')
    sports_sources = get_sources('sports')
    technology_sources = get_sources('technology')
    entertainment_sources = get_sources('entertainment')
    title = 'News Of  The Day'
    return render_template('index.html', title=title, sources=sources, sports_sources=sports_sources, technology_sources=technology_sources, entertainment_sources=entertainment_sources)