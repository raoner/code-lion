from django.urls import path
from polls import views

urlpatterns = [
    path("home/", views.survay_home),
    path("create/", views.survay_create),
    
]