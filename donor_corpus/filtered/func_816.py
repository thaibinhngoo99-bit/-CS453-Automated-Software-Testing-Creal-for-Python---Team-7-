def main(episodes, render, monitor):
    env = gym.make('CartPole-v0')
    q = Q(env.action_space.n, env.observation_space, bin_size=[7, 7, 7, 7], low_bound=[-5, -0.5, -5, -0.5], high_bound=[5, 0.5, 5, 0.5])
    agent = Agent(q, epsilon=0.05)
    learning_decay = lambda lr, t: 1 / (t + 1) ** 0.5
    epsilon_decay = lambda eps, t: 1 / (t + 1) ** 0.5
    trainer = Trainer(agent, gamma=0.95, learning_rate=0.1, learning_rate_decay=learning_decay, epsilon=1.0, epsilon_decay=epsilon_decay, max_step=250)
    if monitor:
        env.monitor.start(RECORD_PATH)
    trainer.train(env, episode_count=episodes, render=render)
    if monitor:
        env.monitor.close()