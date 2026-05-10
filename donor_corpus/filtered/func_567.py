async def hello(websocket, path):
    global players
    jogador = Player(players, 500, 500)

    async def moveUP():
        while 1:
            jogador.setY(jogador.getY() - jogador.speed)
            websocket.send('move:' + str(jogador.id) + ':' + str(jogador.getX()) + ':' + str(jogador.getY()))
            print('move:' + str(jogador.id) + ':' + str(jogador.getX()) + ':' + str(jogador.getY()))
            time.sleep(1)

    async def moveR():
        while 1:
            jogador.setX(jogador.getX() + jogador.speed)
            await websocket.send('move:' + str(jogador.id) + ':' + str(jogador.getX()) + ':' + str(jogador.getY()))
            print('move:' + str(jogador.id) + ':' + str(jogador.getX()) + ':' + str(jogador.getY()))
            time.sleep(1)

    def threadEvoque():
        global players
        loop = asyncio.new_event_loop()
        task = loop.create_task(moveUP())
        loop.run_until_complete(task)
        players += 1
        print(players)

    def threadEvoque2():
        global players
        loop = asyncio.new_event_loop()
        task2 = loop.create_task(moveR())
        loop.run_until_complete(task2)
        players += 1
        print(players)
    while 1:
        msg = await websocket.recv()
        print(msg)
        if msg == 'start':
            players += 1
            await websocket.send('spawn:' + str(players) + ':' + str(jogador.getX()) + ':' + str(jogador.getY()))
            print('spawn:' + str(players) + ':' + str(jogador.getX()) + ':' + str(jogador.getY()))