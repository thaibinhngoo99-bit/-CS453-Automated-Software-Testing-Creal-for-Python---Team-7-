def test_supports_the_type_root_field():
    TestType = GraphQLObjectType('TestType', {'testField': GraphQLField(GraphQLString)})
    schema = GraphQLSchema(TestType)
    request = '{ __type(name: "TestType") { name } }'
    result = execute(schema, object(), parse(request))
    assert not result.errors
    assert result.data == {'__type': {'name': 'TestType'}}