def _parse_json(url, headers={'User-agent': 'Mozilla/5.0'}):
    html = requests.get(url=url, headers=headers).text
    json_str = html.split('root.App.main =')[1].split('(this)')[0].split(';\n}')[0].strip()
    try:
        data = json.loads(json_str)['context']['dispatcher']['stores']['QuoteSummaryStore']
    except:
        return '{}'
    else:
        new_data = json.dumps(data).replace('{}', 'null')
        new_data = re.sub('\\{[\\\'|\\"]raw[\\\'|\\"]:(.*?),(.*?)\\}', '\\1', new_data)
        json_info = json.loads(new_data)
        return json_info