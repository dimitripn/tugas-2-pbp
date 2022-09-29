from django.forms import ModelForm
from todolist.models import MyToDoList

class TaskForm(ModelForm):
    class Meta:
        model = MyToDoList
        fields = ["title", "description"]