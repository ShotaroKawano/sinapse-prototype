from rest_framework import serializers
# from django_filters import rest_framework as filters 
from .models import Like
from .models import Comment
from .models import Board
from .models import Board_Tag
from .models import Tag
from .models import Card
from .models import Arrow
from .models import Arrow_type


#今後dbに合わせて加工必要


class LikeSerializer(serializers.ModelSerializer):
     class Meta:
          model = Like
          fields = ('id','user_id','board_id','created_at')


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
          fields = ('id','user_id','board_id','content','created_at','update_at')

class BoardSerializer(serializers.ModelSerializer):
     # user_id = UserSerializer()

    class Meta:
        model = Board
        fields = ('id','title','description','thumbnail','url_tail','isPublished','created_at','updated_at')

class Board_TagSerializer(serializers.ModelSerializer):
     class Meta:
          model = Board_Tag
          fields = ('id', 'board_id', 'tag_id')

class TagSerializer(serializers.ModelSerializer):
     class Meta:
          model = Tag
          fields = ('id','name')

class CardSerializer(serializers.ModelSerializer):
     class Meta:
          model = Card
          fields = ('id','url','title','summary','thumbnail','positionX','positionY','created_at','updated_at')

class ArrowSerializer(serializers.ModelSerializer):
     class Meta:
          model = Arrow
          fields = ('id','from_card_id','to_card_id','label','arrow_kind_id','board_id','created_at','updated_at')

class Arrow_typeSerializer(serializers.ModelSerializer):
     class Meta:
          model = Arrow_type
          fields = ('id','type')


