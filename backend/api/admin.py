from django.contrib import admin
from .models import Board
from .models import Card
from .models import Like
from .models import Comment
from .models import Tag
from .models import Board_Tag
from .models import Arrow
from .models import Arrow_type
# import pymysql
# Register your models here.

# pymysql.install_as_MySQLdb()

admin.site.register(Board)
admin.site.register(Card)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Board_Tag)
admin.site.register(Arrow)
admin.site.register(Arrow_type)
