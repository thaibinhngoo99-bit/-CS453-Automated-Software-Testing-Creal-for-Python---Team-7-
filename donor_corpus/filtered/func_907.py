def test_respects_the_includedeprecated_parameter_for_enum_values():
    TestEnum = GraphQLEnumType('TestEnum', {'NONDEPRECATED': 0, 'DEPRECATED': GraphQLEnumValue(1, deprecation_reason='Removed in 1.0'), 'ALSONONDEPRECATED': 2})
    TestType = GraphQLObjectType('TestType', {'testEnum': GraphQLField(TestEnum)})
    schema = GraphQLSchema(TestType)
    request = '{__type(name: "TestEnum") {\n        name\n        trueValues: enumValues(includeDeprecated: true) { name }\n        falseValues: enumValues(includeDeprecated: false) { name }\n        omittedValues: enumValues { name }\n    } }'
    result = graphql(schema, request)
    assert not result.errors
    assert sort_lists(result.data) == sort_lists({'__type': {'name': 'TestEnum', 'trueValues': [{'name': 'NONDEPRECATED'}, {'name': 'DEPRECATED'}, {'name': 'ALSONONDEPRECATED'}], 'falseValues': [{'name': 'NONDEPRECATED'}, {'name': 'ALSONONDEPRECATED'}], 'omittedValues': [{'name': 'NONDEPRECATED'}, {'name': 'ALSONONDEPRECATED'}]}})