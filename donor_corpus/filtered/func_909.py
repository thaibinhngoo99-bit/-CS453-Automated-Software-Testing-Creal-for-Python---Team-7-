def test_exposes_descriptions_on_types_and_fields():
    QueryRoot = GraphQLObjectType('QueryRoot', {})
    schema = GraphQLSchema(QueryRoot)
    request = '{\n      schemaType: __type(name: "__Schema") {\n          name,\n          description,\n          fields {\n            name,\n            description\n          }\n        }\n      }\n    '
    result = graphql(schema, request)
    assert not result.errors
    assert sort_lists(result.data) == sort_lists({'schemaType': {'name': '__Schema', 'description': 'A GraphQL Schema defines the capabilities of a ' + 'GraphQL server. It exposes all available types and ' + 'directives on the server, as well as the entry ' + 'points for query and mutation operations.', 'fields': [{'name': 'types', 'description': 'A list of all types supported by this server.'}, {'name': 'queryType', 'description': 'The type that query operations will be rooted at.'}, {'name': 'mutationType', 'description': 'If this server supports mutation, the type that ' + 'mutation operations will be rooted at.'}, {'name': 'directives', 'description': 'A list of all directives supported by this server.'}]}})