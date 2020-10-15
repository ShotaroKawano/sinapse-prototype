
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
# from rest_framework import routers
#黄色い線は気にしなくて良い
from .api.urls import urlpatterns as api_url
from django.views.generic import TemplateView
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls import include, url
from django.conf.urls import url
# from .user.urls import User



# ROUTER = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    # url('api/', include(ROUTER.urls)),
    path('api/', include(api_url)),
    url('auth/', obtain_jwt_token),
    url('user/', include('backend.user.urls')),
]
