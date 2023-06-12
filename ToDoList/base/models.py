from django.db import models

# Create your models here.
class ToDoLists(models.Model):
    task = models.TextField()

    class Meta():
        db_table = 'todolist'
