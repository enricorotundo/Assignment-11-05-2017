#from django.contrib.auth.models import User
from rest_framework import serializers
from single_page_todo.models import User, Todo

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'owner', 'status', 'due_date', 'description')