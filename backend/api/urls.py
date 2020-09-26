from django.conf.urls import include, url
from rest_framework import routers
from backend.api.views import LikeViewSet, index


router = routers.DefaultRouter()
router.register(r'like', LikeViewSet)

urlpatterns = [
    # qiita/api/stock/
    url(r'like/', include(router.urls)),
    url(r'like/', LikeViewSet),
]