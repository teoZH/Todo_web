from django.shortcuts import render, redirect
from todo_app.models import Todo
from django.core.exceptions import ObjectDoesNotExist
from todo_app.forms import TodoInput
from django.http import HttpResponse


def index(request, obj=None):
    todos = Todo.objects.all()
    if request.method == 'POST':
        form = TodoInput(request.POST)
        if form.is_valid():
            todo = Todo(title=request.POST['title'], description=request.POST['description'])
            todo.save()
    else:
        if obj:
            initial_value = {'title': obj.title, 'description': obj.description}
        else:
            initial_value = None
        form = TodoInput(initial=initial_value)
    context = {
        'todos': todos,
        'form': form
    }
    return render(request, 'todo/index.html', context)


def update(request, todo_id):
    if request.method == 'POST':
        try:
            todo = Todo.objects.get(pk=todo_id)
        except ObjectDoesNotExist:
            return redirect('index')
        form = TodoInput(request.POST)
        if form.is_valid():
            form.cleaned_data.update({'id': todo_id})
            todo = Todo(**form.cleaned_data)
            todo.save()
            return redirect('index')
    else:
        try:
            todo = Todo.objects.get(pk=todo_id)
        except ObjectDoesNotExist:
            return redirect('index')

        return index(request, todo)


def delete(request, todo_id):
    try:
        todo = Todo.objects.get(pk=todo_id)
        todo.delete()
    except ObjectDoesNotExist:
        return redirect('index')
    return redirect('index')
