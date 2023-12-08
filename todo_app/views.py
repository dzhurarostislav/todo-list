from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from todo_app.models import Task, Tag


class TodoListView(generic.ListView):
    model = Task
    template_name = "todo_app/todo-list.html"
    ordering = ("is_done", "-created_at")


class TodoCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    template_name = "todo_app/todo-create.html"
    success_url = reverse_lazy("todo_app:todo-list")


class TodoUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    template_name = "todo_app/todo-create.html"
    success_url = reverse_lazy("todo_app:todo-list")


class TodoDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo_app/todo-delete.html"
    success_url = reverse_lazy("todo_app:todo-list")


def change_is_done(request: HttpRequest, pk: int) -> HttpResponse:
    task = Task.objects.get(id=pk)
    is_done = task.is_done
    task.is_done = not is_done
    task.save()
    return redirect("todo_app:todo-list")


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo_app/tag-list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "todo_app/tag-create.html"
    success_url = reverse_lazy("todo_app:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "todo_app/tag-create.html"
    success_url = reverse_lazy("todo_app:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo_app/tag-delete.html"
    success_url = reverse_lazy("todo_app:tag-list")
