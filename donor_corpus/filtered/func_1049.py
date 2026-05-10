def get_dependencies(package):
    url = 'https://pypi.org/pypi/{}/json'
    json = requests.get(url.format(package)).json()
    print(json.keys())