from django.conf import settings
from django.http.response import HttpResponse
# from rest_framework import viewsets
# from django_filters import rest_framework as filters
# from .serializers import LikeFilter
# import os
from .models import Like
from .serializers import LikeSerializer

from rest_framework import generics
from .serializers import BoardSerializer
from .models import Comment
from .serializers import CommentSerializer
from .models import Board
from .serializers import BoardSerializer
from .models import Board_Tags
from .serializers import Board_TagsSerializer
from .models import Tag
from .serializers import TagSerializer
from .models import Card
from .serializers import CardSerializer
from .models import Arrow
from .serializers import ArrowSerializer
from .models import Arrow_type
from .serializers import Arrow_typeSerializer

from rest_framework.viewsets import ModelViewSet



# Create your views here.
class BoardViewSets(ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    # APIのフィルタで使えるフィールドを指定

    def get_queryset(self):
        queryset = Board.objects.all()
        title = self.request.query_params.get("title", None)
        if title is not None:
#部分一致検索ロジック
            queryset = queryset.filter(title__icontains=title)
        return queryset



class CardViewSets(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    # APIのフィルタで使えるフィールドを指定
    # filter_fields = ('id','url','title','summary','thumbnail','positionX','PositionY','created_at','updated_at')



class LikeViewSets(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    # APIのフィルタで使えるフィールドを指定
    # filter_class = LikeFilter
    # filter_fields = ('id','user_id','board_id')



class CommentViewSets(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # APIのフィルタで使えるフィールドを指定


# generics.ListCreateAPIView
# class BoardDetailViewSets(ModelViewSet):
#     queryset = Board.objects.all()
#     serializer_class = BoardSerializer



class TagViewSets(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    # APIのフィルタで使えるフィールドを指定



class BoardTagsViewSets(ModelViewSet):
    queryset = Board_Tags.objects.all()
    serializer_class = Board_TagsSerializer

# APIのフィルタで使えるフィールドを指定
#     filter_fields = ('id')



class ArrowTypeViewSets(ModelViewSet):
    queryset = Arrow.objects.all()
    serializer_class = Arrow_typeSerializer
    # APIのフィルタで使えるフィールドを指定
    # filter_fields = ('id','type')



class ArrowViewSets(ModelViewSet):
    queryset = Arrow.objects.all()
    serializer_class = ArrowSerializer
    # APIのフィルタで使えるフィールドを指定
    # filter_fields = ('id','from_card_id','to_card_id','label','arrow_type_id','created_at','updated_at')
