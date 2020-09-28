from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework import routers
from backend.api.urls import urlpatterns as api_url



ROUTER = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    # url('api/', include(ROUTER.urls)),
    url(r'^api/', include(api_url)),
]

