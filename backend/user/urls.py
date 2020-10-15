from django.conf.urls import include, url
from rest_framework import routers
from .views import AuthRegister, AuthInfoGetView, AuthInfoUpdateView, AuthInfoDeleteView
from django.views.generic.base import RedirectView


urlpatterns = [
    # url('', name='user_index'),
    url('register/$', AuthRegister.as_view()),
    url('mypage/$', AuthInfoGetView.as_view()),
    url('auth_update/$', AuthInfoUpdateView.as_view()),
    url('delete/$', AuthInfoDeleteView.as_view()),
]