
from django.urls import path #

from exercises import views #


urlpatterns = [ #
    path("css01/", views.css01),
    path("css02/", views.css02),
    path("css03/", views.css03),
    path("css04/", views.css04),
    path("flex01/", views.flex01),
    path("flex02/", views.flex02),
    path("position01/", views.position01),
    path("position02/", views.position02),
    path("position03/", views.position03),
]