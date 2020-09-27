from rest_framework import serializers
from backend.api.models import Like


class LikeSerializer(serializers.ModelSerializer):
     class Meta:
          model = Like
          fields = ('created_at')
