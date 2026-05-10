def get_planted_info(cookie, sid, account):
    name_list = []
    planted_id_list = []
    position_list = []
    shop_id_list = []
    url = 'https://xinruimz-isv.isvjcloud.com/papi/get_home_info'
    headers = {'Connection': 'keep-alive', 'Accept': 'application/x.jd-school-raffle.v1+json', 'Authorization': cookie, 'Referer': f'https://xinruimz-isv.isvjcloud.com/plantation/?sid={sid}&un_area=19_1655_4866_0', 'Host': 'xinruimz-isv.isvjcloud.com', 'User-Agent': userAgent(), 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh-Hans;q=0.9'}
    response = requests.get(url=url, verify=False, headers=headers)
    result = response.json()
    planted_list = result['plant_info']
    for i in range(len(planted_list)):
        try:
            name = result['plant_info'][f'{i + 1}']['data']['name']
            planted_id = result['plant_info'][f'{i + 1}']['data']['id']
            position = result['plant_info'][f'{i + 1}']['data']['position']
            shop_id = result['plant_info'][f'{i + 1}']['data']['shop_id']
            name_list.append(name)
            planted_id_list.append(planted_id)
            position_list.append(position)
            shop_id_list.append(shop_id)
            print(f'账号{account}种植的种子为', name, 'planted_id:', planted_id, ',shop_id:', shop_id)
        except Exception as e:
            pass
    return (name_list, position_list, shop_id_list, planted_id_list)