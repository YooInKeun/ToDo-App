from django.shortcuts import render
from django.views.generic import CreateView, ListView

from todo.models import Todo

class TodoMOMCV(ListView, CreateView):
    template_name = 'todo/todo_form_list.html'