from django.conf.urls import include, url
from rest_framework import routers
# from .views import LikeViewSet, index
from .views import LikeViewSet
from .views import CommentViewSet
from .views import BoardViewSet
from .views import Board_TagViewSet
from .views import TagViewSet
from .views import CardViewSet
from .views import ArrowViewSet
from .views import Arrow_TypeViewSet


router = routers.DefaultRouter()
router.register(r'like', LikeViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'board', BoardViewSet)
router.register(r'board_tag', Board_TagViewSet)
router.register(r'Tag', TagViewSet)
router.register(r'card', CardViewSet)


urlpatterns = [
    # qiita/api/stock/
########################################
    url(r'like/', include(router.urls)),
    url(r'like/', LikeViewSet),
########################################
    url(r'comment/', include(router.urls)),
    url(r'like/', CommentViewSet),
########################################
    url(r'board/', include(router.urls)),
    url(r'board/', BoardViewSet),
########################################
    url(r'board_tag/', include(router.urls)),
    url(r'board_tag/', Board_TagViewSet),
########################################
    url(r'tag/', include(router.urls)),
    url(r'tag/', TagViewSet),
########################################
    url(r'card/', include(router.urls)),
    url(r'card/', CardViewSet),   
########################################
    url(r'arrow/', include(router.urls)),
    url(r'arrow/', ArrowViewSet),   
########################################
    url(r'arrow_type/', include(router.urls)),
    url(r'arrow_type/', Arrow_TypeViewSet),   
]
