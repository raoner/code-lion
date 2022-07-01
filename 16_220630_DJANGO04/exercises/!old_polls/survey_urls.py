from django.urls import path
from old_polls import views

urlpatterns = [
    path("survey/",views.survey)
]