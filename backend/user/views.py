from django.contrib.auth import authenticate
from django.db import transaction
from django.http import HttpResponse, Http404
from rest_framework import authentication, permissions, generics
from rest_framework_jwt.settings import api_settings
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.views import APIView
# from user.serializer import UsertSerializer
from .models import User, UserManager
from django.shortcuts import render

from .models import User
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserSerializer

from rest_framework.authentication import BasicAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# def index(request):
#     contexts = {}
#     return render(request,'user/index.html',contexts)



# ユーザ作成のView(POST)
class AuthRegister(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @transaction.atomic
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ユーザ情報取得のView(GET)
class AuthInfoGetView(generics.RetrieveAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, format=None):
        return Response(data={
            'id': request.user.id,
            'username': request.user.username,
            'email': request.user.email,
            # 'profile': request.user.profile,
            },
            status=status.HTTP_200_OK)


# ユーザ情報更新のView(PUT)
class AuthInfoUpdateView(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        try:
            instance = self.queryset.get(pk=self.request.user.uuid)
            return instance
        except User.DoesNotExist:
            raise Http404


# ユーザ削除のView(DELETE)
class AuthInfoDeleteView(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        try:
            instance = self.queryset.get(pk=self.request.user.uuid)
            return instance
        except User.DoesNotExist:
            raise Http404
