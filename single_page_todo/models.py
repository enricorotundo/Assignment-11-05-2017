from __future__ import unicode_literals

from django.db import models
from django.conf import settings

class User(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    username = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'User'



class Todo(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    owner = models.IntegerField()
    status = models.CharField(max_length=10)
    due_date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'Todo'
