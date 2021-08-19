from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200 ,null=True)
    email = models.EmailField(max_length=200,null=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self) :
        return self.name 


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    todo_name = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)

    def __str__(self) :
        return self.todo_name


