from django.contrib import admin
from django.urls import path, include

from todo_app.views import (
    TodoListView,
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView,
    change_is_done,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path("", TodoListView.as_view(), name="todo-list"),
    path("/create/", TodoCreateView.as_view(), name="todo-create"),
    path("/update/<int:pk>/", TodoUpdateView.as_view(), name="todo-update"),
    path("/delete/<int:pk>/", TodoDeleteView.as_view(), name="todo-delete"),
    path("/change_is_done/<int:pk>/", change_is_done, name="change-is-done"),
    path("/tags/", TagListView.as_view(), name="tag-list"),
    path("/tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("/tags/update/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
    path("/tags/delete/<int:pk>/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "todo_app"
