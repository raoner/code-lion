from django.urls import path
from nn_board import views

app_name = "nn-board"

urlpatterns = [
    path("home/", views.home, name = "home"),
    path("post/create/", views.post_create, name = "create"),
    path("post/<int:target_id>/read/", views.post_read, name = "read"),
    path("post/<int:target_id>/update/", views.post_update, name = "update"),
    path("post/<int:target_id>/delete/", views.post_delete, name = "delete"),
    path("landing/", views.landing_index, name = "landing"),
]
