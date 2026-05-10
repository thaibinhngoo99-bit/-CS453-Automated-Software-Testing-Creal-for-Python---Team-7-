def test_identifies_deprecated_enum_values():
    TestEnum = GraphQLEnumType('TestEnum', {'NONDEPRECATED': 0, 'DEPRECATED': GraphQLEnumValue(1, deprecation_reason='Removed in 1.0'), 'ALSONONDEPRECATED': 2})
    TestType = GraphQLObjectType('TestType', {'testEnum': GraphQLField(TestEnum)})
    schema = GraphQLSchema(TestType)
    request = '{__type(name: "TestEnum") {\n        name\n        enumValues(includeDeprecated: true) {\n            name\n            isDeprecated\n            deprecationReason\n        }\n    } }'
    result = graphql(schema, request)
    assert not result.errors
    assert sort_lists(result.data) == sort_lists({'__type': {'name': 'TestEnum', 'enumValues': [{'name': 'NONDEPRECATED', 'isDeprecated': False, 'deprecationReason': None}, {'name': 'DEPRECATED', 'isDeprecated': True, 'deprecationReason': 'Removed in 1.0'}, {'name': 'ALSONONDEPRECATED', 'isDeprecated': False, 'deprecationReason': None}]}})