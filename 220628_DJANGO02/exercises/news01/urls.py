from django.urls import path
from news01 import views

urlpatterns = [
    path("news01/", views.news01),
]
