from django.shortcuts import render
from rest_framework import viewsets
from single_page_todo.serializers import UserSerializer, TodoSerializer
from single_page_todo.models import User, Todo

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer