def test_identifies_deprecated_fields():
    TestType = GraphQLObjectType('TestType', {'nonDeprecated': GraphQLField(GraphQLString), 'deprecated': GraphQLField(GraphQLString, deprecation_reason='Removed in 1.0')})
    schema = GraphQLSchema(TestType)
    request = '{__type(name: "TestType") {\n        name\n        fields(includeDeprecated: true) {\n            name\n            isDeprecated\n            deprecationReason\n        }\n    } }'
    result = graphql(schema, request)
    assert not result.errors
    assert sort_lists(result.data) == sort_lists({'__type': {'name': 'TestType', 'fields': [{'name': 'nonDeprecated', 'isDeprecated': False, 'deprecationReason': None}, {'name': 'deprecated', 'isDeprecated': True, 'deprecationReason': 'Removed in 1.0'}]}})