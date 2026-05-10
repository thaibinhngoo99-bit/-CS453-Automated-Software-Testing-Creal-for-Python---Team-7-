def run():
    with open('results/winner-pickle-' + fn_results, 'rb') as f:
        c = pickle.load(f)
    print('loaded genome:')
    print(c)
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward-small')
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
    net = neat.nn.FeedForwardNetwork.create(c, config)
    register()
    env = gym.make('PuyoPuyoEndlessSmall-v2')
    done = False
    ob = env.reset()
    count = 0
    total_reward = 0
    while True:
        env.render()
        time.sleep(0.5)
        pieces_sum, field_sum = multiplyMatrices(ob[0], ob[1])
        next_piece = pieces_sum[0]
        inp_piece = np.ndarray.flatten(next_piece)
        inp_field = np.ndarray.flatten(field_sum)
        inputs = np.hstack([inp_piece, inp_field])
        nn_output = net.activate(inputs)
        action = np.argmax(nn_output)
        ob, rew, done, info = env.step(action)
        total_reward += rew
        count += 1
        if done:
            break
    print('Game played for ', count, ' turns.')
    print('Total score: ', total_reward)
    if DRAW_NETS:
        visualize.draw_net(config, c, view=True, filename='results/winner-' + fn_results + '.net')
        visualize.draw_net(config, c, view=True, filename='results/winner-' + fn_results + '-enabled.net', show_disabled=False)
        visualize.draw_net(config, c, view=True, filename='results/winner-' + fn_results + '-pruned.net', show_disabled=False, prune_unused=True)