from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField()
    password = models.TextField()

    class Meta():
        db_table = 'User'
