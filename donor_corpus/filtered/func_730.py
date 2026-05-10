def tell_gobbelz(text):
    import requests
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    data = {'text': text}
    requests.post('http://kiosk.shack:8080/say/', data=json.dumps(data), headers=headers)