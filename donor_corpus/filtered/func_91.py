def test_lock_unlock(commander, hook):
    with commander.executest(hook, '!lock'):
        hook.assert_success('Bot is now in ADMIN only mode')
    with commander.executest(hook, '!time', 'goodlikebot'):
        hook.assert_silent_failure()
    with commander.executest(hook, '!lock'):
        hook.assert_success('Bot no longer in ADMIN only mode')
    with commander.executest(hook, '!time', 'goodlikebot'):
        hook.assert_success()