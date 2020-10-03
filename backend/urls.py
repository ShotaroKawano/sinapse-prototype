
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
# from rest_framework import routers
#黄色い線は気にしなくて良い
from backend.api.urls import urlpatterns as api_url
from django.views.generic import TemplateView



# ROUTER = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    # url('api/', include(ROUTER.urls)),
    path('api/', include(api_url)),
]
