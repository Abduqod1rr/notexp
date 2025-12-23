from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("write/", views.addToDo.as_view(), name="write"),
    path("delete/<int:pk>", views.deleteToDo.as_view(), name="delete"),
    path("toggle_todo/<int:pk>", views.toggle_todo_status, name="toggle_todo")
]
