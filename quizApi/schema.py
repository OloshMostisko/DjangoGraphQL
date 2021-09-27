from graphene_django import DjangoObjectType
import graphene
from .models import Board as BoardModel

class Board(DjangoObjectType):
    class Meta:
        model = BoardModel
        

class Query(graphene.ObjectType):
    boards = graphene.List(BoardModel)

    def resolve_boards(root, info):
        return BoardModel.objects.all()

schema = graphene.Schema(query=Query)