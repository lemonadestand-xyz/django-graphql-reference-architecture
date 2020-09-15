from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import User


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = ['username', ]
        interfaces = (relay.Node,)


class Query(ObjectType):
    user = relay.Node.Field(UserNode)
    users = DjangoFilterConnectionField(UserNode)
