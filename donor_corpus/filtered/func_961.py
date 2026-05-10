@app.route('/users')
def list_users():
    page = requests.get('https://chaturbate.com/').text
    user_names = re.findall('<div class="details">\\s*<div class="title">\\s*<a\\s*href=\\s*"/(.+?)/">', page)
    pool = gevent.pool.Pool(10)
    stream_urls = pool.map(get_user_stream, user_names)
    users = [{'name': name, 'stream': stream} for name, stream in zip(user_names, stream_urls) if stream]
    return flask.Response(json.dumps(users), mimetype='application/json')