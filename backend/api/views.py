from django.conf import settings
from django.http.response import HttpResponse
from rest_framework import viewsets
from django_filters import rest_framework as filters
import os

from backend.api.models import Like
from .serializers import LikeSerializer
# from .serializers import LikeFilter

from backend.api.models import Comment
from .serializers import CommentSerializer
from backend.api.models import Board
from .serializers import BoardSerializer
from backend.api.models import Board_Tag
from .serializers import Board_TagSerializer
from backend.api.models import Tag
from .serializers import TagSerializer
from backend.api.models import Card
from .serializers import CardSerializer
from backend.api.models import Arrow
from .serializers import ArrowSerializer
from .serializers import Arrow_TypeSerializer
from .serializers import Arrow_TypeSerializer




# Create your views here.

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    # APIのフィルタで使えるフィールドを指定
    # filter_class = LikeFilter 
    filter_fields = ('created_at')

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # APIのフィルタで使えるフィールドを指定
    filter_fields = ('id','content','created_at','updated_at')

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    # APIのフィルタで使えるフィールドを指定
    filter_fields = ('id','title','description','thunbnail','url_tail','isPublished','created_at','updated_at')

class Board_TagViewSet(viewsets.ModelViewSet):
    queryset = Board_Tag.objects.all()
    serializer_class = Board_TagSerializer
    # APIのフィルタで使えるフィールドを指定
    filter_fields = ('id')

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = Board_TagSerializer
    # APIのフィルタで使えるフィールドを指定
    filter_fields = ('id','name')

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = Board_TagSerializer
    # APIのフィルタで使えるフィールドを指定
    filter_fields = ('id','url','title','summary','thumbnail','positionX','PositionY','created_at','updated_at')


class ArrowViewSet(viewsets.ModelViewSet):
    queryset = Arrow.objects.all()
    serializer_class = ArrowSerializer
    # APIのフィルタで使えるフィールドを指定
    filter_fields = ('id','from_card_id','to_card_id','label','arrow_type_id','created_at','updated_at')

class Arrow_TypeViewSet(viewsets.ModelViewSet):
    queryset = Arrow.objects.all()
    serializer_class = Arrow_TypeSerializer
    # APIのフィルタで使えるフィールドを指定
    filter_fields = ('id','type')
