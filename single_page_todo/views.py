from rest_framework import viewsets
from single_page_todo.serializers import UserSerializer, TodoSerializer
from single_page_todo.models import User, Todo
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import generics, viewsets
from rest_framework.decorators import permission_classes
from rest_framework import permissions

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (permissions.AllowAny,)