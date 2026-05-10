def test_respects_the_includedeprecated_parameter_for_fields():
    TestType = GraphQLObjectType('TestType', {'nonDeprecated': GraphQLField(GraphQLString), 'deprecated': GraphQLField(GraphQLString, deprecation_reason='Removed in 1.0')})
    schema = GraphQLSchema(TestType)
    request = '{__type(name: "TestType") {\n        name\n        trueFields: fields(includeDeprecated: true) { name }\n        falseFields: fields(includeDeprecated: false) { name }\n        omittedFields: fields { name }\n    } }'
    result = graphql(schema, request)
    assert not result.errors
    assert sort_lists(result.data) == sort_lists({'__type': {'name': 'TestType', 'trueFields': [{'name': 'nonDeprecated'}, {'name': 'deprecated'}], 'falseFields': [{'name': 'nonDeprecated'}], 'omittedFields': [{'name': 'nonDeprecated'}]}})