from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MyToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(null = False, blank = False, auto_now_add = True)
    title = models.CharField(max_length = 255)
    description = models.TextField()
    is_finished = models.BooleanField(default = False)

