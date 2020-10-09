
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
# from rest_framework import routers
#黄色い線は気にしなくて良い
from backend.api.urls import urlpatterns as api_url


from django.views.generic import TemplateView

from django_registration.backends.one_step.views import RegistrationView

from .urls import include, path

from .users.forms import CustomUserForm




# ROUTER = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    # url('api/', include(ROUTER.urls)),
    path('api/', include(api_url)),

    # path("api-auth/",include),
    #     path("accounts/",
    #      include("django_registration.backends.one_step.urls")),
    path("accounts/register/",
         RegistrationView.as_view(
             form_class=CustomUserForm,
             success_url="/",
             ), name="django_registration_register"), 

    path("accounts/",
         include("django_registration.backends.one_step.urls")),
 

    path("accounts/",
         include("django.contrib.auth.urls")),

    # path("api/",
    #      include("users.api.urls")),

    # path("api/",
    #      include("questions.api.urls")),

    path("api-auth/",
         include("rest_framework.urls")),

    path("api/rest-auth/",
         include("rest_auth.urls")),
        
    path("api/rest-auth/registration/",
         include("rest_auth.registration.urls")),
]
