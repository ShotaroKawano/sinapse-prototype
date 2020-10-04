# from django.conf.urls import include, url
from rest_framework import routers
from django.urls import path, include
from .views import BoardViewSets
from .views import LikeViewSets
from .views import CommentViewSets
from .views import BoardTagsViewSets
from .views import TagViewSets
from .views import CardViewSets
from .views import ArrowViewSets
from .views import ArrowTypeViewSets
# from django.views.generic import TemplateView


router = routers.DefaultRouter()
router.register(r'likes', LikeViewSets)
router.register(r'comments', CommentViewSets)
router.register(r'boards', BoardViewSets)
router.register(r'board_tags', BoardTagsViewSets)
router.register(r'tags', TagViewSets)
router.register(r'cards', CardViewSets)
router.register(r'arrows', ArrowViewSets)
router.register(r'arrow_types', ArrowTypeViewSets)


urlpatterns = [
    path('', include(router.urls)),
    # path('boards/', BoardViewSets.as_view())
    # qiita/api/stock/
########################################
    # url(r'like/', include(router.urls)),
    # path('like/', LikeView.as_view()),
########################################
#     url(r'comment/', include(router.urls)),
    # path('comment/', CommentView.as_view()),
# ########################################
    # url(r'board/', include(router.urls)),
    # path('board/', BoardView.as_view()),
    # path('board/<int:pk>', BoardDetailView.as_view()),
########################################
    # url(r'board_tag/', include(router.urls)),
    # path('board_tag/', Board_TagView.as_view()),
########################################
    # url(r'tag/', include(router.urls)),
    # path('tag/',TagView.as_view()),
#########################################
    # path(r'card/', include(router.urls)),
    # path('card/', CardView.as_view()),
# ########################################
#     url(r'arrow/', include(router.urls)),
    # path('arrow/', ArrowView.as_view()),
# ########################################
#     url(r'arrow_kind/', include(router.urls)),
    # path('arrow_type/', Arrow_typeView.as_view()),
]
