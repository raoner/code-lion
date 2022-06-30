
from django.urls import path
from blog import views

urlpatterns = [
	path("home/", views.blog_home),
	path("create/", views.create),
	path("read/", views.read),
	path("update/", views.update),
	path("delete/", views.delete),
	# path("home/create/", views.create),
	# path("home/read/", views.read),
	# path("home/update/", views.update),
	# path("home/delete/", views.delete),
]
