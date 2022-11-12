from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.page, name="page"),
    path("?q", views.pageSearch, name="search"),
    path("new", views.pageNew, name="new"),
    path("saved", views.entrySave, name="save"),
]
