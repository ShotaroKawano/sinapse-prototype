from django.conf import settings
from django.http.response import HttpResponse
from rest_framework import viewsets
import os
from backend.api.models import Like
from backend.api.serializer import LikeSerializer


# Create your views here.

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    # APIのフィルタで使えるフィールドを指定
    filter_fields = ('created_at')