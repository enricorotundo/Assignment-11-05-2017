from single_page_todo.serializers import UserSerializer, TodoSerializer
from single_page_todo.models import User, Todo
from rest_framework import viewsets
from rest_framework import permissions

class TodoViewSet(viewsets.ModelViewSet):
    """ Binds together model and serializer for TODO items """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (permissions.AllowAny,)

