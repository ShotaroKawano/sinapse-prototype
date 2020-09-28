from rest_framework import serializers
# from django_filters import rest_framework as filters 
from backend.api.models import Like
from backend.api.models import Comment
from backend.api.models import Board
from backend.api.models import Board_Tag
from backend.api.models import Tag
from backend.api.models import Card
from backend.api.models import Arrow


#今後dbに合わせて加工必要


class LikeSerializer(serializers.ModelSerializer):
     class Meta:
          model = Like
          fields = ('created_at')


# class LikeFilter(filters.FilterSet):
# # フィルタの定義
# created = filters.DateTimeFilter(lookup_expr='gt')
# class Meta:
#      model = Like
#      # フィルタを列挙する。
#      # デフォルトの検索方法でいいなら、モデルフィールド名のフィルタを直接定義できる。
#      fields = ['created_at']




class CommentSerializer(serializers.ModelSerializer):
     class Meta:
          model = Comment
          fields = ('id','content','created_at','updated_at')

class BoardSerializer(serializers.ModelSerializer):
     class Meta:
          model = Board
          fields = ('id','title','description','thunbnail','url_tail','isPublished','created_at','updated_at')

class Board_TagSerializer(serializers.ModelSerializer):
     class Meta:
          model = Board_Tag
          fields = ('id')

class TagSerializer(serializers.ModelSerializer):
     class Meta:
          model = Tag
          fields = ('id','name')

class CardSerializer(serializers.ModelSerializer):
     class Meta:
          model = Card
          fields = ('id','url','title','summary','thumbnail','positionX','PositionY','created_at','updated_at')

class ArrowSerializer(serializers.ModelSerializer):
     class Meta:
          model = Card
          fields = ('id','from_card_id','to_card_id','label','arrow_type_id','created_at','updated_at')

class Arrow_TypeSerializer(serializers.ModelSerializer):
     class Meta:
          model = Card
          fields = ('id','type')


