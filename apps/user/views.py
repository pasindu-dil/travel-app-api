from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from apps.user.serializers import UserSerializer

class  UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer