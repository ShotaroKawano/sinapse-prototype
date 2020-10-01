# from django.conf.urls import include, url
# from rest_framework import routers
from django.urls import path, include
from .views import BoardView
from .views import LikeView
from .views import CommentView
from .views import Board_TagView
from .views import TagView
from .views import CardView
from .views import ArrowView
from .views import Arrow_typeView
# from django.views.generic import TemplateView


# router = routers.DefaultRouter()
# router.register(r'like', LikeViewSet)
# router.register(r'comment', CommentViewSet)
# router.register(r'board', BoardViewSet)
# router.register(r'board_tag', Board_TagViewSet)
# router.register(r'Tag', TagViewSet)
# router.register(r'card', CardViewSet)


urlpatterns = [
    # qiita/api/stock/
########################################
    # url(r'like/', include(router.urls)),
    path('like/', LikeView.as_view()),
########################################
#     url(r'comment/', include(router.urls)),
    path('comment/', CommentView.as_view()),
# ########################################
    # url(r'board/', include(router.urls)),
    path('board/', BoardView.as_view()),
########################################
    # url(r'board_tag/', include(router.urls)),
    path('board_tag/', Board_TagView.as_view()),
########################################
    # url(r'tag/', include(router.urls)),
    path('tag/',TagView.as_view()),
#########################################
    # path(r'card/', include(router.urls)),
    path('card/', CardView.as_view()),   
# ########################################
#     url(r'arrow/', include(router.urls)),
    path('arrow/', ArrowView.as_view()),   
# ########################################
#     url(r'arrow_kind/', include(router.urls)),
    path('arrow_type/', Arrow_typeView.as_view()),   
]
