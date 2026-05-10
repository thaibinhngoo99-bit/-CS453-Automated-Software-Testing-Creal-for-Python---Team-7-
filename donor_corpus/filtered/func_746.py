def update_episode_proto(episode_proto, minitaur, action, step):
    """Update the episode proto by appending the states/action of the minitaur.

  Note that the state/data over max_num_steps preallocated
  (len(episode_proto.state_action)) will not be stored in the proto.
  Args:
    episode_proto: The proto that holds the state/action data for the current
      episode.
    minitaur: The minitaur instance. See envs.minitaur for details.
    action: The action applied at this time step. The action is an 8-element
      numpy floating-point array.
    step: The current step index.
  """
    max_num_steps = len(episode_proto.state_action)
    if step >= max_num_steps:
        tf.logging.warning('{}th step is not recorded in the logging since only {} steps were pre-allocated.'.format(step, max_num_steps))
        return
    step_log = episode_proto.state_action[step]
    step_log.info_valid = minitaur.IsObservationValid()
    time_in_seconds = minitaur.GetTimeSinceReset()
    step_log.time.seconds = int(time_in_seconds)
    step_log.time.nanos = int((time_in_seconds - int(time_in_seconds)) * 1000000000.0)
    motor_angles = minitaur.GetMotorAngles()
    motor_velocities = minitaur.GetMotorVelocities()
    motor_torques = minitaur.GetMotorTorques()
    for i in range(minitaur.num_motors):
        step_log.motor_states[i].angle = motor_angles[i]
        step_log.motor_states[i].velocity = motor_velocities[i]
        step_log.motor_states[i].torque = motor_torques[i]
        step_log.motor_states[i].action = action[i]
    _update_base_state(step_log.base_position, minitaur.GetBasePosition())
    _update_base_state(step_log.base_orientation, minitaur.GetBaseRollPitchYaw())
    _update_base_state(step_log.base_angular_vel, minitaur.GetBaseRollPitchYawRate())