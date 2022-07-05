from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=128)
    category_general = models.CharField(max_length=32)
    category_details = models.CharField(max_length=32)
    content = models.TextField()
    press_name = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)


class Press(models.Model):
    name = models.CharField(max_length=32)
    founded_at = models.DateTimeField(auto_now_add=True)
