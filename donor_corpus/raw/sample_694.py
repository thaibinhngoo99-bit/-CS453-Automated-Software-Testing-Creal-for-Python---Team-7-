import graphene
from graphene import Node
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.rest_framework.mutation import SerializerMutation
from graphene_django.types import DjangoObjectType
from rest_framework.generics import get_object_or_404

from contact.models import Contact
from contact.serializers import ContactSerializer


class ContactModelMutation(SerializerMutation):
    class Meta:
        serializer_class = ContactSerializer
        convert_choices_to_enum = False


class ContactNode(DjangoObjectType):
    class Meta:
        model = Contact
        interfaces = (Node,)
        fields = "__all__"
        filter_fields = ["first_name"]


class ContactType(DjangoObjectType):
    class Meta:
        model = Contact
        fields = "__all__"


class Query(graphene.ObjectType):
    contact_node = Node.Field(ContactNode)
    contacts_node = DjangoFilterConnectionField(ContactNode)

    contact = graphene.Field(ContactType, id=graphene.Int())
    contacts = graphene.List(ContactType)

    def resolve_contacts(self, info, **kwargs):
        return Contact.objects.all()

    def resolve_contact(self, info, id):
        return get_object_or_404(Contact, pk=id)


class DeleteMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        id = graphene.Int(required=True)

    # The class attributes define the response of the mutation
    id = graphene.ID()
    message = graphene.String()

    @classmethod
    def mutate(cls, root, info, id):
        contact = get_object_or_404(Contact, pk=id)
        contact.delete()
        return cls(id=id, message='deleted')


class Mutation(graphene.ObjectType):
    create_contact = ContactModelMutation.Field()
    update_contact = ContactModelMutation.Field()
    delete_contact = DeleteMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
