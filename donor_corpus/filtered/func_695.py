def playGame(model):
    score = 0
    done = False
    action = 0
    frame = np.zeros((1, FRAME_SIZE))
    previous_frame = np.zeros((1, FRAME_SIZE))
    env.reset()
    observation_dim = list(INPUT_SHAPE)
    observation_dim.insert(0, 1)
    observation_dim = tuple(observation_dim)
    while not done:
        env.render()
        observation, reward, done, _ = env.step(action)
        frame = np.reshape(observation[:, :, 0], (1, FRAME_SIZE))
        frame = np.where(frame > 0, 1.0, 0)
        difference = frame - previous_frame
        final_observation = np.zeros((1, INPUT_DIM))
        final_observation[0, :FRAME_SIZE] = frame
        final_observation[0, FRAME_SIZE:] = difference
        final_observation = np.reshape(final_observation, observation_dim)
        prediction = model.predict(final_observation)
        action = convert_prediction_to_action(prediction)
        score += reward
        writeCsv(2, score)
        previous_frame = np.copy(frame)
    return score