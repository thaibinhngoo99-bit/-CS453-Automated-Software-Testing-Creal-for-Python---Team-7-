def _parse_earnings_json(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}):
    resp = requests.get(url, headers=headers)
    content = resp.content.decode(encoding='utf-8', errors='strict')
    page_data = [row for row in content.split('\n') if row.startswith('root.App.main = ')][0][:-1]
    page_data = page_data.split('root.App.main = ', 1)[1]
    return json.loads(page_data)