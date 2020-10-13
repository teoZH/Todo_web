from django.shortcuts import render
from todo_app.models import Todo
from django.http import HttpResponse


def index(request):
    todos = Todo.objects.all()
    context = {
        'todos':todos
    }
    return render(request, 'todo/index.html',context)
