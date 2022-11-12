from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.page, name="page"),
    path("?q", views.pageSearch, name="search"),
    path("new", views.pageNew, name="new"),
    path("save", views.entrySave, name="save"),
    path("edit", views.entryEdit, name="edit"),
    path("saveEdit", views.saveEdit, name="saveEdit"),
    path("randomEntry", views.randomEntry, name="randomEntry")
]
