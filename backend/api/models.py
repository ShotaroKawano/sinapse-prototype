from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    pass



class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Board(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    thumbnail = models.CharField(blank=True,null=True,max_length=255)
    url_tail = models.CharField(blank=True,null=True,max_length=255)
    is_published = models.BooleanField(default=True)
    user = models.ForeignKey(User, related_name='user_boards', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 多対多のrelated_nameはこちらにつけるべきなのかもしれない
    # likes = models.ManyToManyField(User, through='Like', related_name='likes')
    # comments1 = models.ManyToManyField(User, through='Comment', related_name='comments2')
    # tags = models.ManyToManyField(Tag, through='Board_Tag', related_name='tags')
    # ManyToManyをBoardではない方のテーブルにつければいいのでは？

    def __str__(self):
        return self.title



class Card(models.Model):
    url = models.CharField(max_length=2083)
    title = models.CharField(max_length=255)
    summary = models.TextField(blank=True,null=True)
    thumbnail = models.CharField(blank=True,null=True,max_length=2083)
    position_x = models.IntegerField()
    position_y = models.IntegerField()
    board = models.ForeignKey(Board, related_name='board_cards', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # arrows = models.ManyToManyField('self', through='Arrow', related_name='arrows')

    def __str__(self):
        return self.title + ' ' + self.url



class Like(models.Model):
    user = models.ForeignKey(User, related_name='user_likes', on_delete=models.CASCADE)
    board = models.ForeignKey(Board, related_name='board_likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.board.title + ' liked by ' + self.user.username
        # return self.board


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='user_comments', on_delete=models.CASCADE)
    board = models.ForeignKey(Board, related_name='board_comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.board.title + ' commented by ' + self.user.username + ' ' + self.content



class Board_Tag(models.Model):
    board = models.ForeignKey(Board, related_name='board_tags', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name='tag_boards',  on_delete=models.CASCADE)

    def __str__(self):
        return self.board.title + ' tagged with ' + self.tag.name



class Arrow_type(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.type



class Arrow(models.Model):
    from_card = models.ForeignKey('Card', related_name='board_from_cards', on_delete=models.CASCADE)
    from_position = models.CharField(max_length=255)
    to_card = models.ForeignKey('Card', related_name='board_to_cards', on_delete=models.CASCADE)
    to_position = models.CharField(max_length=255)
    label = models.CharField(blank=True,null=True,max_length=255)
    arrow_type = models.ForeignKey('Arrow_type', on_delete=models.CASCADE)
    board = models.ForeignKey(Board, related_name='board_arrows', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.label
