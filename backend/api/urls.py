from django.conf.urls import include, url
from rest_framework import routers
# from .views import LikeViewSet, index
from .views import LikeViewSet


router = routers.DefaultRouter()
router.register(r'like', LikeViewSet)

urlpatterns = [
    # qiita/api/stock/
    url(r'like/', include(router.urls)),
    url(r'like/', LikeViewSet),
]
