from django.urls import path
from todolist.views import register, login_user, show_todolist, logout_user, add_task, delete_task, update_task

app_name = 'todolist'

urlpatterns = [    
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('create-task/', add_task, name='add_task'),
    path('delete-task/<int:task_id>/', delete_task, name='delete_task'),
    path('update-task/<int:task_id>/', update_task, name='update_task'),
]