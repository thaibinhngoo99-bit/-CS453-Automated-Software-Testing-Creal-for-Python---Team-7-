def test_list_build_source_namespaces(github_trigger):
    namespaces_expected = [{'personal': True, 'score': 1, 'avatar_url': 'avatarurl', 'id': 'knownuser', 'title': 'knownuser', 'url': 'https://bitbucket.org/knownuser'}, {'score': 0, 'title': 'someorg', 'personal': False, 'url': '', 'avatar_url': 'avatarurl', 'id': 'someorg'}]
    found = github_trigger.list_build_source_namespaces()
    found.sort()
    namespaces_expected.sort()
    assert found == namespaces_expected