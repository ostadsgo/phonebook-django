from django.urls import path

from . import views


urlpatterns = [
   path("", views.index, name="home"),
   path("group/", views.bakhtar_group, name="group"),

]

