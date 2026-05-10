def fertilization(cookie, plant_id, shop_id, account):
    url = 'https://xinruimz-isv.isvjcloud.com/papi/fertilization'
    headers = {'Connection': 'keep-alive', 'Accept': 'application/x.jd-school-raffle.v1+json', 'Authorization': cookie, 'Referer': f'https://xinruimz-isv.isvjcloud.com/plantation/shop_index/?shop_id={shop_id}&channel=index', 'Host': 'xinruimz-isv.isvjcloud.com', 'User-Agent': userAgent(), 'Accept-Language': 'zh-CN,zh-Hans;q=0.9', 'Content-Type': 'application/json;charset=utf-8'}
    data = '{"plant_id":' + f'{plant_id}' + '}'
    i = 1
    while True:
        try:
            response = requests.post(url=url, verify=False, headers=headers, data=data)
            result = response.json()
            level = result['level']
            complete_level = result['complete_level']
            printT('【账号{0}】【plant_id:{3}】成功施肥10g，当前等级{1}，种子成熟等级为{2}'.format(account, level, complete_level, plant_id))
            time.sleep(5)
            i += 1
        except Exception as e:
            message = result['message']
            total = i * 10
            if '肥料不足' in message:
                msg('【账号{0}】【plant_id:{1}】本次一共施肥{2}g'.format(account, plant_id, total))
                printT('【账号{0}】【plant_id:{1}】肥料不足10g'.format(account, plant_id))
                break