from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse

import datetime

from todolist.forms import TaskForm
from todolist.models import MyToDoList

# Create your views here.
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login_user')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse('todolist:show_todolist'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login_user'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_tasks = MyToDoList.objects.filter(user=request.user)
    context = {'data_tasks':data_tasks,
               'user' : request.user,
               'last_login': request.COOKIES['last_login'],}
    return render(request, 'todolist.html', context)

@login_required(login_url='/todolist/login/')
def add_task(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('todolist:show_todolist')
        
    context = {'form':form}
    return render(request, 'add_task.html', context)

@login_required(login_url='/todolist/login/')
def delete_task(request, task_id):
    task = MyToDoList.objects.get(id=task_id)
    if task:
        task.delete()
        return redirect('todolist:show_todolist')
    messages.error(request, 'Tidak dapat menghapus task!')
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def update_task(request, task_id):
    task = MyToDoList.objects.get(id=task_id)
    if task.is_finished:
        task.is_finished = False
    else:
        task.is_finished = True
    task.save()
    return redirect('todolist:show_todolist')
    