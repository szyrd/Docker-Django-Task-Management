from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('task_list')  # Redirect to the task list
    else:
        form = UserCreationForm()
    return render(request, 'taskmanag/register.html', {'form': form})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'taskmanag/add_task.html', {'form': form})

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'taskmanag/edit_task.html', {'form': form})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    task.delete()
    return redirect('task_list')

@login_required
def view_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    return render(request, 'taskmanag/view_task.html', {'task': task})

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'taskmanag/task_list.html', {'tasks': tasks})


