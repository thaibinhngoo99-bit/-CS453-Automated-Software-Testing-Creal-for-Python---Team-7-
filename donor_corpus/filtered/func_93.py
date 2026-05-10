def test_rank(users, hook):
    with Rank(us=users).executest(hook, args=''):
        hook.assert_failure('Try !rank RANK NICK')
    with Rank(us=users).executest(hook, args='just_rank'):
        hook.assert_failure('Try !rank RANK NICK')
    with Rank(us=users).executest(hook, args='BAD_RANK goodlikebot'):
        hook.assert_failure('BAD_RANK is not a valid rank')
    with Rank(us=users).executest(hook, args='BAN goodlikebot'), users._manual('goodlikebot'):
        hook.assert_success('goodlikebot is now BAN')
        assert_that(users.rank('goodlikebot')).is_equal_to(UserRank.BAN)
    users.set_use_elastic(False)
    with Rank(us=users).executest(hook, args='ADMIN goodlikebot'):
        hook.assert_failure('Rank could not be set')