from django.db import models
from django.contrib.auth.models import User


# usersはdjangoのデフォルト機能を利用

class Board(models.Model):
    title = models.CharField('タイトル', max_length=255,null=True)
    description = models.CharField('ディスクリプション', max_length=500,null=True)
    thumbnail = models.CharField('サムネイル', max_length=255, null=True)
    url_tail = models.CharField('テイル', max_length=255,null=True)
    isPublished = models.BooleanField(default=True,null=True) 
    user = models.ForeignKey(User, related_name='boards', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)




    # user =  models.ForeignKey(User, related_name=‘boards’, on_delete=models.CASCADE)
    # user = models.ManyToManyField(
    #     User,
    #     through="Like",
    # )
    # created_at = models.DateTimeField('作成日時', auto_now_add=True)
    # update_at = models.DateTimeField('更新日時', auto_now=True)

    def __str__(self):
        return self.title



class Card(models.Model):
    URL = models.CharField('URL', max_length=255,null=True)
    title = models.CharField('タイトル', max_length=255,null=True)
    summary = models.CharField('サマリー', max_length=500,null=True)
    thumbnail = models.CharField('サムネイル', max_length=255,null=True)
    positionX = models.IntegerField('x座標',null=True)
    positionY = models.IntegerField('y座標',null=True)
    board = models.ForeignKey(Board,on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField('作成日時', auto_now_add=True,null=True)
    update_at = models.DateTimeField('更新日時', auto_now=True,null=True)

    # def __str__(self):
    #     return self.title



class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
  

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    update_at = models.DateTimeField('更新日時', auto_now=True)


class Tag(models.Model):
    name = models.CharField('タグ', max_length=255, null=True)



class Board_Tag(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
 

class Arrow(models.Model):
    from_card_id = models.IntegerField('フロムカード')
    to_card_id = models.IntegerField('トゥーカード')
    label = models.CharField('ラベル',max_length=255)
    arrow_type_id = models.IntegerField('アロータイプ')
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)


class Arrow_type(models.Model):
    type = models.CharField('アロータイプ',max_length=255)




