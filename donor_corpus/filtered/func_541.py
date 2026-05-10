def start():
    global cookie, cookies
    print(f'\n【准备开始...】\n')
    nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f8')
    if cookie != '':
        account = setName(cookie)
        access_token = get_ck(cookie, sid_ck, account)
        cookie = get_Authorization(access_token, account)
        name_list, position_list, shop_id_list, planted_id_list = get_planted_info(cookie, sid, account)
        taskName_list, taskId_list, taskName_list2, taskId_list2, taskName_list3, taskId_list3 = get_task(cookie, account)
        get_water(cookie, position_list, sid, account)
        get_fertilizer(cookie, shop_id_list, account)
        for i, j in zip(taskName_list, taskId_list):
            do_task1(cookie, i, j, account)
        for i, j in zip(taskName_list2, taskId_list2):
            do_task2(cookie, i, j, account)
        for i, j in zip(taskName_list3, taskId_list3):
            do_task3(cookie, i, j, sid, account)
        flag = 0
        for i in shop_id_list:
            do_fertilizer_task(cookie, i, account)
        for k in shop_id_list:
            taskName_list2, taskId_list2, taskName_list3, taskId_list3, taskName_list4, taskId_list4 = get_fertilizer_task(cookie, k, account)
            do_fertilizer_task4(cookie, k, account)
            do_fertilizer_task5(cookie, k, account)
            if beauty_plant_exchange == 'true':
                do_fertilizer_task6(cookie, k, account)
            for i, j in zip(taskName_list2, taskId_list2):
                print(i, j, k)
                do_fertilizer_task2(cookie, i, j, k, account)
            for i, j in zip(taskName_list3, taskId_list3):
                print(i, j, k)
                do_fertilizer_task3(cookie, i, j, k, account)
            if choose_plant_id == 'false':
                for i in planted_id_list:
                    watering(cookie, i, sid, account)
                    fertilization(cookie, i, k, account)
            else:
                fertilization(cookie, planted_id_list[flag], k, account)
                watering(cookie, planted_id, sid, account)
            flag += 1
    elif cookies != '':
        for cookie, planted_id in zip(cookies, planted_ids):
            try:
                account = setName(cookie)
                access_token = get_ck(cookie, sid_ck, account)
                cookie = get_Authorization(access_token, account)
                name_list, position_list, shop_id_list, planted_id_list = get_planted_info(cookie, sid, account)
            except Exception as e:
                pass
        for cookie, planted_id in zip(cookies, planted_ids):
            try:
                account = setName(cookie)
                access_token = get_ck(cookie, sid_ck, account)
                cookie = get_Authorization(access_token, account)
                name_list, position_list, shop_id_list, planted_id_list = get_planted_info(cookie, sid, account)
                taskName_list, taskId_list, taskName_list2, taskId_list2, taskName_list3, taskId_list3 = get_task(cookie, account)
                get_water(cookie, position_list, sid, account)
                get_fertilizer(cookie, shop_id_list, account)
                for i, j in zip(taskName_list, taskId_list):
                    do_task1(cookie, i, j, account)
                for i, j in zip(taskName_list2, taskId_list2):
                    do_task2(cookie, i, j, account)
                for i, j in zip(taskName_list3, taskId_list3):
                    do_task3(cookie, i, j, sid, account)
                flag = 0
                for i in shop_id_list:
                    do_fertilizer_task(cookie, i, account)
                for k in shop_id_list:
                    taskName_list2, taskId_list2, taskName_list3, taskId_list3, taskName_list4, taskId_list4 = get_fertilizer_task(cookie, k, account)
                    do_fertilizer_task4(cookie, k, account)
                    do_fertilizer_task5(cookie, k, account)
                    if beauty_plant_exchange == 'true':
                        do_fertilizer_task6(cookie, k, account)
                    for i, j in zip(taskName_list2, taskId_list2):
                        print(i, j, k)
                        do_fertilizer_task2(cookie, i, j, k, account)
                    for i, j in zip(taskName_list3, taskId_list3):
                        print(i, j, k)
                        do_fertilizer_task3(cookie, i, j, k, account)
                    if choose_plant_id == 'false':
                        for i in planted_id_list:
                            fertilization(cookie, i, k, account)
                            watering(cookie, i, sid, account)
                    else:
                        print('【账号{}现在开始施肥】'.format(account))
                        fertilization(cookie, planted_id_list[flag], k, account)
                        print('【账号{}现在开始浇水】'.format(account))
                        watering(cookie, planted_id, sid, account)
                    flag += 1
            except Exception as e:
                pass
    else:
        printT('请检查变量plant_cookie是否已填写')