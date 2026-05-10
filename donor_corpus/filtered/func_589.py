@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    verbose = False or debugging
    error = request.args.get('error')
    return make_response(render_template('makeGame.html', title='Welcome', cool=123, error=error))