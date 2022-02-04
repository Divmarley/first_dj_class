
from django.urls import path

from todo.views import *
app_name='todos'
urlpatterns = [
    path("todo", todo_view, name="index"),
    path("delete/<int:id>", delete_todo, name="delete"),
]
