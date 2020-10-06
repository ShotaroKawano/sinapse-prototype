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

# from django.contrib.auth.models import User
from .models import User


#今後dbに合わせて加工必要
class UserSerializer(serializers.ModelSerializer):
     class Meta:
          model = User
          fields = ('id', 'username',)



class ArrowTypeSerializer(serializers.ModelSerializer):

     class Meta:
          model = Arrow_type
          # fields = ('id','arrows')
          fields = '__all__'



class ArrowSerializer(serializers.ModelSerializer):
     arrow_types = ArrowTypeSerializer(read_only=True)

     class Meta:
          model = Arrow
          # fields = ('id','from_card','to_card','label','arrow_type_id','board_id','created_at','updated_at','arrow_types')
          fields = '__all__'



class CardSerializer(serializers.ModelSerializer):
     # boards = BoardSerializer(many=True, read_only=True)
     # board_from_cards = ArrowSerializer(many=True, read_only=True)
     # board = serializers.IntegerField(read_only=True)

     class Meta:
          model = Card
          # fields = ('id','url','title','summary','thumbnail','position_x','position_y','created_at','updated_at','boards')
          # fields = ('id','url','title','summary','thumbnail','board_arrows','created_at','updated_at')
          fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
     # user_comments = UserSerializer(read_only=True)
     user = UserSerializer(read_only=True)

     class Meta:
          model = Comment
          # fields = ('id','user_id','board_id','content','created_at','update_at')
          # fields = ('id','user','board','content','created_at','updated_at')
          # fields = ('id','username')
          fields = '__all__'
          # depth = 2


class LikeSerializer(serializers.ModelSerializer):
     class Meta:
          model = Like
          # fields = ('id','user_id','board_id','created_at')
          fields = '__all__'



class TagSerializer(serializers.ModelSerializer):
     class Meta:
          model = Tag
          # fields = ('id','name')
          fields = '__all__'



class BoardTagSerializer(serializers.ModelSerializer):
     # tag_boards = TagSerializer(many=True, read_only=True)
     # tag = TagSerializer()
     # tag = serializers.DictField(source='tag')

     class Meta:
          model = Board_Tag
          fields = ('tag',)
          # fields = '__all__'
          depth = 2



class BoardSerializer(serializers.ModelSerializer):
     # user_id = UserSerializer(read_only=True)
     user_id = serializers.IntegerField(write_only=True)
     like_count = serializers.SerializerMethodField()
     comment_count = serializers.SerializerMethodField()
     user = UserSerializer(read_only=True)
     board_tags = BoardTagSerializer(many=True, read_only=True)
     board_cards = CardSerializer(many=True, read_only=True)
     board_comments = CommentSerializer(many=True, read_only=True)
     # board_cards = serializers.StringRelatedField()
     # cards = 'neko'

     class Meta:
          model = Board
          fields = ('id', 'title', 'description', 'thumbnail', 'url_tail', 'is_published', 'created_at', 'updated_at', 'like_count', 'comment_count', 'user', 'board_tags', 'board_cards', 'board_comments','user_id')
          # fields = '__all__'
          # depth = 2

     def get_like_count(self, instance):
          return instance.board_likes.count()

     def get_comment_count(self, instance):
          return instance.board_comments.count()

     def create(self, validated_data):
          # user = validated_data.pop('user')
          # board = Board.objects.create(**validated_data)
          print('/////////////////////')
          print(validated_data)
          print('/////////////////////')
          board = Board.objects.create(**validated_data)
          # board.save()
          return board



# class LikeFilter(filters.FilterSet):
# # フィルタの定義
# created = filters.DateTimeFilter(lookup_expr='gt')
# class Meta:
#      model = Like
#      # フィルタを列挙する。
#      # デフォルトの検索方法でいいなら、モデルフィールド名のフィルタを直接定義できる。
#      fields = ['created_at']
