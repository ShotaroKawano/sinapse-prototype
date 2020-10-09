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
from .models import Board_Tag
from .serializers import BoardTagSerializer
from .models import Tag
from .serializers import TagSerializer
from .models import Card
from .serializers import CardSerializer
from .models import Arrow
from .serializers import ArrowSerializer
from .models import Arrow_type
from .serializers import ArrowTypeSerializer

from rest_framework.viewsets import ModelViewSet
# from rest_framework import generics

# スクレイピングfunction関連
from django.views.decorators.csrf import csrf_exempt
from urllib.request import Request, urlopen
import urllib.request
# from bs4 import BeautifulSoup
import json
from django.http import HttpResponse


# Create your views here.
class BoardViewSets(ModelViewSet):
# class BoardViewSets(generics.ListCreateAPIView):
    # queryset = Board.objects.all()
    # なんで降順にならないの
    queryset = Board.objects.all().order_by('-id')
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
    def get_queryset(self):
        queryset = Card.objects.all()
        board_id = self.request.query_params.get("board_id", None)
        if board_id is not None:
            #部分一致検索ロジック
            queryset = queryset.filter(board_id=board_id)
        return queryset



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
    queryset = Board_Tag.objects.all()
    serializer_class = BoardTagSerializer

# APIのフィルタで使えるフィールドを指定
#     filter_fields = ('id')



class ArrowTypeViewSets(ModelViewSet):
    queryset = Arrow.objects.all()
    serializer_class = ArrowTypeSerializer
    # APIのフィルタで使えるフィールドを指定
    # filter_fields = ('id','type')



class ArrowViewSets(ModelViewSet):
    queryset = Arrow.objects.all()
    serializer_class = ArrowSerializer
    # APIのフィルタで使えるフィールドを指定
    # filter_fields = ('id','from_card_id','to_card_id','label','arrow_type_id','created_at','updated_at')
    def get_queryset(self):
        queryset = Arrow.objects.all()
        board_id = self.request.query_params.get("board_id", None)
        if board_id is not None:
            #部分一致検索ロジック
            queryset = queryset.filter(board_id=board_id)
        return queryset



@csrf_exempt
def getInfo(request):
    json_str = request.body
    print(json_str)
    json_data = json.loads(json_str)
    print(json_data)
    url = json_data['url']
    print(url)
    # list = []
    dict ={}

    req = Request(url, headers={'User-Agent': 'XYZ/3.0'})

    html = urlopen(req, timeout=10).read()
    soup = BeautifulSoup(html, "html.parser")

    head_info = soup.find('head')
    meta_img = head_info.find('meta', {'property' : 'og:image'})
    soup_img = meta_img['content']
    meta_description = head_info.find('meta', {'property' : 'og:description'})
    soup_desc = meta_description['content']
    soup_title = head_info.find('title').getText()

    # list.append([soup_title, soup_desc, soup_img])
    dict.update({'soup_title': soup_title})
    dict.update({'soup_desc': soup_desc})
    dict.update({'soup_img': soup_img})

    # context = {'list':list}
    context = {'dict':dict}

    # return HttpResponse(json.dumps(list))
    return HttpResponse(json.dumps(dict))
