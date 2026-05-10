def test_fails_as_expected_on_the_type_root_field_without_an_arg():
    TestType = GraphQLObjectType('TestType', {'testField': GraphQLField(GraphQLString)})
    schema = GraphQLSchema(TestType)
    request = '\n    {\n        __type {\n           name\n        }\n    }'
    result = graphql(schema, request)
    expected_error = {'message': ProvidedNonNullArguments.missing_field_arg_message('__type', 'name', 'String!'), 'locations': [SourceLocation(line=3, column=9)]}
    assert expected_error in [format_error(error) for error in result.errors]