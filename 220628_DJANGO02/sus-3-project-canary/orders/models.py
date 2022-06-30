from django.db import models


class Diner(models.Model):
    name = models.CharField(max_length=64)
    category = models.CharField(max_length=32)
    address = models.CharField(max_length=256)
    open_at = models.TimeField()
    close_at = models.TimeField()


class Menu(models.Model):
    name = models.CharField(max_length=32)
    price = models.IntegerField()


class Order(models.Model):
    address = models.CharField(max_length=256)
    ordered_at = models.DateTimeField(auto_now_add=True)
    estimated_duration = models.IntegerField()
