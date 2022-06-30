from unicodedata import category
from django.db import models

# Create your models here.

class NewsDocument(models.Model):
    title = models.CharField(max_length=128)
    sub_category = models.CharField(max_length=128)
    large_category= models.CharField(max_length=128)
    written_media = models.CharField(max_length=128)
    content = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    

class Media(models.Model):
    name = models.CharField(max_length=128)
    dateOfEstablishment = models.DateTimeField()
    