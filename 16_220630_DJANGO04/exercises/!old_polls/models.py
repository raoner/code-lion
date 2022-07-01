from sys import maxsize
from django.db import models

# Create your models here.

class Article(models.Model):
    age = models.IntegerField()
    sex = models.BooleanField()
    residence = models.CharField(max_length=128)
    residential_suggestions = models.TextField()    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)