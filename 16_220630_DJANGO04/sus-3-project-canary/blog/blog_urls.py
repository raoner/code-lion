from django.urls import path

from blog import views


urlpatterns = [
    path("home/", views.blog_home),
    path("create/", views.blog_post_create),
    path("<int:target_id>/read/", views.blog_post_read),
    path("<int:target_id>/update/", views.blog_post_update),
    path("<int:target_id>/delete/", views.blog_post_delete),
]
