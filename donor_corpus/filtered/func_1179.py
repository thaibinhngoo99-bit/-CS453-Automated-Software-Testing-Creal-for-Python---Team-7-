@pytest.mark.parametrize('payload, expected_error, expected_message', [('{"zen": true}', SkipRequestException, ''), ('{}', InvalidPayloadException, "Missing 'repository' on request"), ('{"repository": "foo"}', InvalidPayloadException, "Missing 'owner' on repository"), ('{\n    "repository": {\n      "owner": {\n        "name": "someguy"\n      },\n      "name": "somerepo",\n      "ssh_url": "someurl"\n    },\n    "ref": "refs/tags/foo",\n    "head_commit": {\n      "id": "11d6fbc",\n      "url": "http://some/url",\n      "message": "some message",\n      "timestamp": "NOW"\n    }\n  }', None, None), ('{\n    "repository": {\n      "owner": {\n        "name": "someguy"\n      },\n      "name": "somerepo",\n      "ssh_url": "someurl"\n    },\n    "ref": "refs/tags/foo",\n    "head_commit": {\n      "id": "11d6fbc",\n      "url": "http://some/url",\n      "message": "[skip build]",\n      "timestamp": "NOW"\n    }\n  }', SkipRequestException, '')])
def test_handle_trigger_request(github_trigger, payload, expected_error, expected_message):

    def get_payload():
        return json.loads(payload)
    request = AttrDict(dict(get_json=get_payload))
    if expected_error is not None:
        with pytest.raises(expected_error) as ipe:
            github_trigger.handle_trigger_request(request)
        assert str(ipe.value) == expected_message
    else:
        assert isinstance(github_trigger.handle_trigger_request(request), PreparedBuild)